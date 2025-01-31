import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import plotly.express as px
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Função de tratamento de exceções ao carregar dados
def safe_load_data(url):
    try:
        tables = pd.read_html(url)
        return pd.DataFrame(tables[2]).drop(0)
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return None

# CSS personalizado para botões, rótulos e elementos
st.markdown("""
    <style>
        .st-info-box {
            background-color: #1e1e1e;
            padding: 15px;
            border-radius: 8px;
            color: white;
            border-left: 5px solid #FF0055;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# Título do aplicativo
#st.title("Análise da Variação Relativa das Variáveis Econômicas")
# Caixa de informações
st.markdown("""
### Explorando a Volatilidade do Preço do Petróleo
<div class="st-info-box">
O mercado de petróleo é influenciado por fatores econômicos, geopolíticos e de oferta e demanda global. Este dashboard oferece uma visão holística da variação do preço do petróleo Brent e suas relações com outras variáveis econômicas.
</div>
<br/>
""", unsafe_allow_html=True)

# Importar os dados do petróleo
df = safe_load_data("http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view")
if df is not None:
    df.columns = ['Data', 'Preço - petróleo bruto (Brent) - em dólares']
    df['Preço - petróleo bruto (Brent) - em dólares'] = df['Preço - petróleo bruto (Brent) - em dólares'].apply(lambda x: float(x[:-2] + '.' + x[-2:]))
    df.rename(columns={'Data': 'Date'}, inplace=True)
    df['Date'] = pd.to_datetime(df['Date']).dt.tz_localize(None)

    # Filtrar dados a partir de 2006
    data_corte_min = pd.to_datetime('2006-01-01')
    base = df[df['Date'] >= data_corte_min]

    # Obter dados adicionais
    def get_yahoo_data(ticker):
        try:
            data = yf.Ticker(ticker).history(period="max", interval="1d").reset_index()
            data['Date'] = data['Date'].dt.tz_localize(None)
            return data[['Date', 'Close']]
        except Exception as e:
            st.error(f"Erro ao carregar dados de {ticker}: {e}")
            return None

    s500 = get_yahoo_data("^GSPC").rename(columns={'Close': 'S&P500'})
    gold_history = get_yahoo_data("IAU").rename(columns={'Close': 'Gold'})
    dxy_history = get_yahoo_data("DX-Y.NYB").rename(columns={'Close': 'Índice DXY'})

    # Mesclar dados
    base = base.merge(s500, on='Date', how='left').merge(gold_history, on='Date', how='left').merge(dxy_history, on='Date', how='left').fillna(method='ffill')

    # Normalizar os dados
    cols_to_normalize = ['Preço - petróleo bruto (Brent) - em dólares', 'S&P500', 'Gold', 'Índice DXY']
    base[cols_to_normalize] = base[cols_to_normalize].apply(lambda x: x / x.iloc[0])

    # Menu de filtros
    st.sidebar.header("Filtros")
    tickers_selecionados = st.sidebar.multiselect(
        "Selecione as variáveis que deseja visualizar",
        options=cols_to_normalize,
        default=cols_to_normalize
    )

    min_date, max_date = base['Date'].min().date(), base['Date'].max().date()
    start_date, end_date = st.sidebar.slider("Selecione o período:", min_value=min_date, max_value=max_date, value=(min_date, max_date), format="YYYY-MM-DD")
    df_filtered = base[(base['Date'] >= pd.Timestamp(start_date)) & (base['Date'] <= pd.Timestamp(end_date))]

# Funções para cada aba
def Estatistica_descritiva():
    # Estatísticas descritivas melhoradas
    st.markdown("##### Estatísticas Descritivas - Preço do Petróleo Brent")
    
    desc_stats = base[['Preço - petróleo bruto (Brent) - em dólares']].describe()

    # Destacando estatísticas importantes em cartões visuais
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="📊 Média do Preço", value=f"{desc_stats.loc['mean'][0]:.2f} USD")
    with col2:
        st.metric(label="🔺 Preço Máximo", value=f"{desc_stats.loc['max'][0]:.2f} USD")
    with col3:
        st.metric(label="🔻 Preço Mínimo", value=f"{desc_stats.loc['min'][0]:.2f} USD")
    with col4:
        st.metric(label="📉 Volatilidade (Desvio Padrão)", value=f"{desc_stats.loc['std'][0]:.2f} USD")

    # Insights explicativos
    st.markdown("""
    ---
    ##### 🔍 Principais Insights
    - **Média:** O preço médio do petróleo Brent foi de **{:.2f}** dólares, indicando relativa estabilidade em períodos não influenciados por choques econômicos.
    - **Máximo:** O pico de **{:.2f}** dólares está associado a choques externos, como crises de oferta de energia.
    - **Mínimo:** O preço mínimo de **{:.2f}** dólares pode ter ocorrido durante períodos de recessão global.
    - **Desvio Padrão:** Com **{:.2f}** dólares, a volatilidade sugere grandes oscilações, possivelmente causadas por crises geopolíticas.
    ---
    """.format(desc_stats.loc['mean'][0], desc_stats.loc['max'][0], desc_stats.loc['min'][0], desc_stats.loc['std'][0]))

    # Gráfico de distribuição do preço do petróleo
    st.markdown("""##### 📈 Distribuição do Preço do Petróleo Brent
O histograma abaixo mostra a distribuição dos preços normalizados do petróleo Brent ao longo do tempo.
    """)
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(base['Preço - petróleo bruto (Brent) - em dólares'], bins=30, kde=True, ax=ax)
    ax.set_title("Distribuição do Preço do Petróleo Brent")
    st.pyplot(fig)
    st.markdown("""
- **Distribuição assimétrica levemente positiva:** A maior concentração dos preços está entre **0.75** e **1.25** dólares normalizados, indicando um período predominante de estabilidade.
- **Picos distintos:** O segundo pico próximo de **1.50** dólares sugere um momento de aumento acentuado dos preços, possivelmente associado a eventos econômicos específicos, como a crise financeira de 2008 ou o conflito Rússia-Ucrânia.
- **Cauda longa:** A presença de uma cauda à direita evidencia episódios de preços elevados, característicos de choques de oferta ou alta demanda no mercado energético global.
    """)
    



def Grafico_Var_Event_Hist():
    # Verifique se há pelo menos uma variável selecionada
     if not tickers_selecionados:
        st.warning("Por favor, selecione pelo menos uma variável para visualizar o gráfico.")
     else:
        # Gráfico interativo com anotações de eventos históricos
        st.markdown("""
### 📈 Gráfico de Variação Relativa com Eventos Históricos
Gráfico interativo mostrando a evolução do preço do petróleo Brent e de variáveis econômicas. As séries normalizadas permitem comparar diferentes tendências, identificar convergências e momentos de ruptura ao longo do tempo.
""")         

        st.markdown("""
---
##### 🛠️ Como utilizar este gráfico:
1. No painel lateral, você pode escolher as variáveis que deseja visualizar.
2. Use o controle deslizante para ajustar o período de interesse. Você pode se concentrar em momentos específicos, como crises econômicas ou períodos de estabilidade.
3. Linhas verticais vermelhas indicam eventos significativos.
---
        """)
        fig = px.line(df_filtered, x='Date', y=tickers_selecionados, title="Variação Relativa das Variáveis ao Longo do Tempo")

        # Eventos históricos
        eventos = {
            '2008-07-01': 'Crise Financeira Global',
            '2020-03-01': 'Início da Pandemia COVID-19',
            '2022-02-24': 'Conflito Rússia-Ucrânia'
        }

        for date, event in eventos.items():
            fig.add_vline(x=date, line_width=2, line_dash="dash", line_color="red")
            fig.add_annotation(x=date, y=1.05, text=event, showarrow=True, arrowhead=1)

        st.plotly_chart(fig)

def Correlacao():
    # Matriz de correlação e heatmap
    st.markdown("#### Matriz de Correlação das Variáveis")
    corr_matrix = base[cols_to_normalize].corr()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=ax)
    st.pyplot(fig)

def Tend_Sazo():
    # Decomposição sazonal
    st.markdown("#### 📊 Análise Temporal: Tendências e Sazonalidade")
    result = seasonal_decompose(base['Preço - petróleo bruto (Brent) - em dólares'], model='multiplicative', period=365)
    fig, axes = plt.subplots(3, 1, figsize=(10, 10))
    result.trend.plot(ax=axes[0], title="Tendência")
    result.seasonal.plot(ax=axes[1], title="Sazonalidade")
    result.resid.plot(ax=axes[2], title="Resíduos")
    st.pyplot(fig)


#Menu tabs 
tabs = st.tabs (['Preço', 'Variações', 'Correlacao', 'Tendências e Sazonalidade'])

# Aba "Preço"
with tabs[0]: 
    Estatistica_descritiva()
# Aba "Variações"
with tabs[1]: 
    Grafico_Var_Event_Hist()
# Aba "Correlacao"
with tabs[2]: 
    Correlacao()
# Aba "Tendências e Sazonalidade"
with tabs[3]: 
    Tend_Sazo()