import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
import plotly.graph_objects as go
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
from sklearn.model_selection import train_test_split
from datetime import date, timedelta
import yfinance as yf
from babel.dates import format_date

# Configurar o título da página e o ícone
st.set_page_config(
    page_title="Modelo Preditivo",  
    page_icon="📈",  
    layout="wide",  
    initial_sidebar_state="expanded"  
)

# Função para calcular métricas
def calculate_metrics(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mape = mean_absolute_percentage_error(y_true, y_pred) * 100
    return mae, mse, rmse, mape

st.markdown("""
    <style>
        h2 { color: #FF0055; font-size: 28px; }
        .stButton>button {
            background-color: #FF0055;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
        }
        .stButton>button:hover { background-color: #e6004c; }
        .st-info-box {
            background-color: #1e1e1e;
            padding: 15px;
            border-radius: 8px;
            color: white;
            border-left: 5px solid #FF0055;
            font-size: 16px;
        }
        .st-observation {
            font-size: 14px;
            color: #555;
            margin-top: -10px;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h2>📈 Previsão do Preço do Petróleo</h2>', unsafe_allow_html=True)

# Data inicial e explicação
DATA_INICIAL = date.today()
data_inicial_formatada = format_date(DATA_INICIAL, format='long', locale='pt_BR')
st.markdown(f"""
<div class="st-info-box">
Defina a data desejada para prever o preço do barril de petróleo. O modelo se baseia no fechamento do dia anterior para calcular as previsões futuras.
Recomendamos previsões de curto prazo (<strong>7 a 15 dias</strong>) para maior precisão, mas você pode explorar até <strong>30 dias</strong> a partir de <strong>{data_inicial_formatada}</strong>.
</div><br/>
""", unsafe_allow_html=True)
st.markdown('<div class="st-observation">* As previsões estão sendo realizadas com base em dados históricos dos últimos 20 anos.</div>', unsafe_allow_html=True)

# Entrada do usuário
diaspred = st.slider("Selecione o número de dias futuros:", min_value=1, max_value=30, value=7, step=1)
st.subheader("Configurações Avançadas")
estimadores = st.slider("Selecione o número de estimadores a ser usado (Representa o número total de árvores de decisão que serão treinadas no modelo, Um número maior pode melhorar a precisão, mas também aumenta o risco de overfitting e o tempo de treinamento.)", min_value=5, max_value=1000, value=200, step=5)
learning = st.slider("Selecione o learning rate a ser usado (Controla o peso de cada nova árvore ao ajustar o modelo, um learning rate baixo exige mais árvores e vice e versa.)", min_value=0.01, max_value=0.8, value=0.1, step=0.01)

# Carregar dados
@st.cache_data
def load_data():
    df = yf.Ticker("BZ=F").history(period="20y", interval="1d").reset_index()
    df['Date'] = pd.to_datetime(df['Date']).dt.tz_localize(None)
    df.rename(columns={'Close': 'Preço - petróleo bruto (Brent) - em dólares'}, inplace=True)
    df = df[['Date', 'Preço - petróleo bruto (Brent) - em dólares']].set_index('Date').dropna()
    return df

def create_time_features(df):
    df['Ano'] = df.index.year
    df['Mês'] = df.index.month
    df['Dia'] = df.index.day
    df['Dia_Semana'] = df.index.weekday
    df['dia_anterior'] = df["Preço - petróleo bruto (Brent) - em dólares"].shift(1).fillna(method='bfill')
    return df

df = load_data()
basef = create_time_features(df)
TARGET = "Preço - petróleo bruto (Brent) - em dólares"
selected_features = ['Ano', 'Mês', 'Dia', 'Dia_Semana', 'dia_anterior']

# Divisão de treino e validação
x = basef[selected_features]
y = basef[TARGET]
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, shuffle=False)

@st.cache_resource
def train_model():
    dtrain = xgb.DMatrix(x_train, label=y_train)
    dval = xgb.DMatrix(x_val, label=y_val)
    params = {
        "objective": "reg:squarederror",
        "learning_rate": learning,
        "max_depth": estimadores,
        "n_jobs": -1
    }
    reg = xgb.train(
        params=params,
        dtrain=dtrain,
        num_boost_round=300,
        evals=[(dval, "validation")],
        early_stopping_rounds=10,
        verbose_eval=False
    )
    return reg

if st.button("Atualizar Dados"):
    st.cache_data.clear()
    st.rerun()

if st.button("Prever"):
    reg = train_model()
    last_n_days = basef.index[-diaspred:]
    x_test, y_test = basef.loc[last_n_days, selected_features], basef.loc[last_n_days, TARGET]
    dtest = xgb.DMatrix(x_test)
    preds_test = reg.predict(dtest)
    mae, mse, rmse, mape = calculate_metrics(y_test, preds_test)
    ultimo_preco = basef[TARGET].iloc[-1]
    confiabilidade = max(0, 100 - mape)

    st.markdown("""

""")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("###### 📉 Preço do Dia Anterior")
        st.write(f"**{ultimo_preco:.2f} USD**")
    with col2:
        st.markdown("###### 📊 Confiabilidade da Previsão")
        st.write(f"**{confiabilidade:.2f}%**")

    future_dates = pd.date_range(start=DATA_INICIAL + timedelta(days=1), periods=diaspred, freq='D')
    future_df = pd.DataFrame(index=future_dates)
    future_df['Ano'] = future_dates.year
    future_df['Mês'] = future_dates.month
    future_df['Dia'] = future_dates.day
    future_df['Dia_Semana'] = future_dates.weekday
    future_df['dia_anterior'] = [ultimo_preco] + [np.nan] * (len(future_dates) - 1)
    future_df['dia_anterior'] = future_df['dia_anterior'].ffill()
    dfuture = xgb.DMatrix(future_df[selected_features])
    future_df['Previsão'] = reg.predict(dfuture)

    df_plot = pd.DataFrame({
        'Data': list(basef.index[-30:]) + list(future_df.index),
        'Preço': list(basef[TARGET].iloc[-30:]) + list(future_df['Previsão']),
        'Tipo': ['Real'] * 30 + ['Previsão'] * len(future_df)
    })

    metricas_texto = f"MAE: {mae:.4f}, MSE: {mse:.4f}, RMSE: {rmse:.4f}, MAPE: {mape:.2f}%"

    # Ponto de transição (último dia real)
    data_transicao = basef.index[-1]

    # Criar o gráfico
    fig = go.Figure()

    # Adicionar dados reais e previsão
    fig.add_trace(go.Scatter(
    x=df_plot['Data'][:30],
    y=df_plot['Preço'][:30],
    mode='lines+markers',
    name='Dados Reais',
    line=dict(color='#5DADE2')  # Azul suave
))
    fig.add_trace(go.Scatter(
    x=df_plot['Data'][30:],
    y=df_plot['Preço'][30:],
    mode='lines+markers',
    name='Previsão',
    line=dict(color='#F4D03F')  # Amarelo ouro suave
))

    # Adicionar linha vertical de transição com a cor da FIAP
    fig.add_shape(
    type='line',
    x0=data_transicao,
    y0=min(df_plot['Preço']) - 5,  # Ajuste do eixo Y para incluir margem
    x1=data_transicao,
    y1=max(df_plot['Preço']) + 5,
    line=dict(color="#FF0055", width=2, dash='dash'),
    name="Linha de Transição"
)

    # Anotação com a cor da FIAP
    fig.add_annotation(
    x=data_transicao,
    y=max(df_plot['Preço']),
    text="Início da Previsão",
    showarrow=True,
    arrowhead=2,
    ax=20,
    ay=-30,
    font=dict(size=12, color="#FF0055"),
    arrowcolor="#FF0055"
)

    # Configurações do layout
    fig.update_layout(
    title="Previsão do Preço do Petróleo (Brent)",
    xaxis_title="Data",
    yaxis_title="Preço (em dólares)",
    annotations=[dict(xref="paper", yref="paper", x=0, y=1.15, text=metricas_texto, showarrow=False)],
    showlegend=True
)

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Previsões Futuras")
    st.dataframe(future_df[['Previsão']].reset_index().rename(columns={'index': 'Data'}))
    st.success("✅ Previsão concluída com sucesso!")
    st.subheader("Confira também: ")
    with st.expander("📋 Explicação das Métricas"):
        st.write("""
        - **MAE (Erro Absoluto Médio):** Média dos erros absolutos entre os valores reais e previstos. Quanto menor, melhor.
        - **MSE (Erro Quadrático Médio):** Média dos erros ao quadrado. Penaliza erros maiores mais fortemente.
        - **RMSE (Raiz do Erro Quadrático Médio):** Raiz quadrada do MSE, mantendo as unidades originais.
        - **MAPE (Erro Absoluto Percentual Médio):** Percentual médio de erro em relação aos valores reais.
        """)

    # Explicação sobre o modelo XGBoost
    with st.expander("🤖 Por que utilizamos o XGBoost?"):
        st.write("""
    O **XGBoost (Extreme Gradient Boosting)** foi escolhido para este projeto devido às seguintes vantagens:
    
    - **Robustez para dados complexos:** O XGBoost é ideal para lidar com dados temporais, especialmente em situações onde existem flutuações rápidas, tendências ou sazonalidades.
    - **Capacidade de lidar com dados não estacionários:** Dados financeiros, como o preço do petróleo, muitas vezes apresentam variações bruscas ao longo do tempo. O XGBoost pode capturar esses padrões de forma eficiente.
    - **Eficiência Computacional:** O modelo é conhecido por seu treinamento rápido e otimização baseada em árvores de decisão, tornando-o uma escolha eficiente mesmo quando lidamos com grandes conjuntos de dados históricos.
    - **Regularização integrada:** O XGBoost possui mecanismos internos para evitar o overfitting, o que é crucial ao prever séries temporais que podem ser voláteis.
    
    Embora o XGBoost não seja um modelo puramente dedicado a séries temporais como o ARIMA ou Prophet, ele é extremamente flexível e pode gerar previsões de alta qualidade ao incorporar variáveis de tempo, como feito neste projeto.
    """)

    with st.expander("📊 O que considerar ao analisar a confiabilidade?"):
        st.write("""
        A métrica de confiabilidade fornece uma visão prática da precisão da previsão:
        
        - **Valores acima de 85%**: Indicam previsões mais seguras e confiáveis. Nesses casos, as diferenças percentuais entre os valores reais e previstos tendem a ser pequenas.
        - **Entre 70% e 85%**: Indicam previsões moderadamente confiáveis. A análise do MAPE pode ajudar a identificar se os erros percentuais são aceitáveis para o seu cenário.
        - **Abaixo de 70%**: Requer atenção, pois indica uma maior variabilidade nas previsões. Avalie se há tendências bruscas no preço do petróleo ou mudanças externas que possam afetar os dados.

        ⚠️ **Importante:** O MAPE é uma métrica complementar à confiabilidade. Sempre verifique o contexto dos dados para interpretar as previsões corretamente.
        """)

    # Rodapé estilizado
st.markdown("""
<div style="text-align: center; margin-top: 30px; color: #999;">
        Criado pela turma <strong>6DTAT de Data Analytics</strong>, FIAP Pós Tech.
    </div>
""", unsafe_allow_html=True) 
    
