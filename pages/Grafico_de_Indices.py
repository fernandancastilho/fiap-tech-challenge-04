import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# ---- TÍTULO E INTRODUÇÃO ----
st.title("Análise da Variação Relativa do Petróleo e Outros Índices 📈🛢️")
st.markdown("""
Este aplicativo analisa a relação entre o preço do petróleo Brent e variáveis econômicas globais, 
como o **S&P 500**, **Ouro (Gold)**, **Índice DXY** e **TASI**.  
""")

# ---- FUNÇÃO PARA OBTER DADOS ----
@st.cache_data
def get_data():
    # Baixar os dados do petróleo
    df = yf.Ticker("BZ=F").history(period="max", interval="1d").reset_index()
    df['Date'] = df['Date'].dt.tz_localize(None)
    df.rename(columns={'Close': 'Preço - petróleo bruto (Brent) - em dólares'}, inplace=True)
    df = df[['Date', 'Preço - petróleo bruto (Brent) - em dólares']]

    # Baixar os dados do S&P 500
    sp500 = yf.Ticker("^GSPC").history(period="max", interval="1d").reset_index()
    sp500['Date'] = sp500['Date'].dt.tz_localize(None)

    # Baixar os dados do ouro
    gold = yf.Ticker("IAU").history(period="max", interval="1d").reset_index()
    gold['Date'] = gold['Date'].dt.tz_localize(None)

    # Baixar o Índice DXY
    dxy = yf.Ticker("DX-Y.NYB").history(period="max", interval="1d").reset_index()
    dxy['Date'] = dxy['Date'].dt.tz_localize(None)

    # Baixar os dados do TASI
    tasi = pd.read_csv(
        'https://raw.githubusercontent.com/ntfcamargo/Base-TECH-CHALLENGE-3/refs/heads/main/Dados%20Hist%C3%B3ricos%20-%20Tadawul%20All%20Share.csv',
        sep=','
    )
    tasi.rename(columns={'Data': 'Date'}, inplace=True)
    tasi['Date'] = pd.to_datetime(tasi['Date'])
    tasi['Último'] = tasi['Último'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)

    # Mesclar os dados
    base = df.merge(sp500[['Date', 'Close']], on='Date', how='left').fillna(method='ffill')
    base.rename(columns={'Close': 'S&P500'}, inplace=True)

    base = base.merge(gold[['Date', 'Close']], on='Date', how='left').fillna(method='ffill')
    base.rename(columns={'Close': 'Gold'}, inplace=True)

    base = base.merge(dxy[['Date', 'Close']], on='Date', how='left').fillna(method='ffill')
    base.rename(columns={'Close': 'Índice DXY'}, inplace=True)

    base['Retorno Diário Petróleo'] = base['Preço - petróleo bruto (Brent) - em dólares'].pct_change().fillna(0)

    basef = base[base['Date'] > '2005-12-31'].merge(tasi[['Date', 'Último']], on='Date', how='left').fillna(method='ffill')
    basef.rename(columns={'Último': 'TASI'}, inplace=True)

    return basef

# ---- OBTENDO OS DADOS ----
basef = get_data()

# ---- DESCRIÇÃO DAS VARIÁVEIS ----
st.header("📊 Descrição das Variáveis")
st.write("Abaixo está uma explicação sobre cada uma das variáveis e sua relação com o preço do petróleo:")

st.subheader("🛢️ Preço do Petróleo Brent")
st.write("""
- **Descrição**: Representa o preço diário do barril de petróleo Brent, referência global.  
- **Relação**: Afetado por oferta, demanda, geopolítica e fatores macroeconômicos.
""")

st.subheader("📈 S&P 500")
st.write("""
- **Descrição**: Índice das 500 maiores empresas americanas.  
- **Relação**: Quando a economia cresce, a demanda por petróleo aumenta, elevando os preços.
""")

st.subheader("🪙 Ouro (Gold)")
st.write("""
- **Descrição**: Metal precioso usado como proteção contra incertezas econômicas.  
- **Relação**: Em crises, investidores migram para o ouro, reduzindo o preço do petróleo (correlação negativa).
""")

st.subheader("💵 Índice DXY")
st.write("""
- **Descrição**: Mede a força do dólar em relação a outras moedas globais.  
- **Relação**: Um dólar mais forte torna o petróleo mais caro para outros países, reduzindo a demanda.
""")

st.subheader("🇸🇦 TASI (Índice da Arábia Saudita)")
st.write("""
- **Descrição**: Principal índice da bolsa da Arábia Saudita.  
- **Relação**: Pode indicar mudanças na política da OPEP, afetando o preço do petróleo.
""")

# ---- NORMALIZAÇÃO DOS DADOS ----
cols_to_normalize = ['Preço - petróleo bruto (Brent) - em dólares', 'S&P500', 'Gold', 'Índice DXY', 'TASI']
df_normalized = basef.copy()
df_normalized[cols_to_normalize] = basef[cols_to_normalize].apply(lambda x: x / x.iloc[0])

# ---- CRIAÇÃO DO GRÁFICO ----
st.header("📉 Variação Relativa das Variáveis")
fig, ax = plt.subplots(figsize=(14, 8))
for col in cols_to_normalize:
    if col == 'Preço - petróleo bruto (Brent) - em dólares':
        ax.plot(df_normalized['Date'], df_normalized[col], label=col, linewidth=2.5, color='red')
    else:
        ax.plot(df_normalized['Date'], df_normalized[col], label=col, linewidth=1.5, alpha=0.7)

ax.set_title("Variação Relativa das Variáveis ao Longo do Tempo", fontsize=16)
ax.set_xlabel("Ano", fontsize=14)
ax.set_ylabel("Variação Relativa (Base 1.0)", fontsize=14)
ax.legend(loc="upper left", fontsize=10)
ax.grid(alpha=0.3)

# Exibir o gráfico no Streamlit
st.pyplot(fig)

# ---- CHECKBOX PARA EXIBIR DADOS ----
if st.checkbox("📋 Exibir tabela de dados"):
    st.write(basef)
