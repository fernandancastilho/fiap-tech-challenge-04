# Verificar se o Streamlit está instalado pip install streamlit
# Verificar se o yfinace está instalado pip install yfinance
# Para a execução do código em streamlit insira no terminal: Streamlit run main.py

#importar as bibliotecas
import streamlit as st
import pandas as pd 
import yfinance as yf
from datetime import timedelta

st.set_page_config(
    page_title="Exploração e Insights",
    page_icon="📊",
    menu_items={"About":"Anderson Cardoso Pinto de Souza ; Fernanda Nogueira Castilho ; Jéssica da Silva Santos ; Nicholas Todescan ; Wagner Silveira Santos"}
)

#criar as funções de carregamento de dados
    #cotações do ITAU - ITUB4 - 2010 até 2024
#Estruturando os dados em uma função para armazenamento dno cache.
@st.cache_data
def carregar_dados(empresas):
    texto_tickers = " ".join(empresas)
    dados_acao = yf.Tickers(texto_tickers)
    cotacoes_acoes = dados_acao.history(period="1d",start="2010-01-01", end="2024-12-31")
    print(cotacoes_acoes)
    cotacoes_acoes = cotacoes_acoes["Close"]
    return cotacoes_acoes

acoes = ["ITUB4.SA", "PETR4.SA","MGLU3.SA","VALE3.SA", "ABEV3.SA", "GGBR4.SA"]
dados = carregar_dados(acoes)

# Criar a interface do streamlit 
st.write("""
# App preço de ações
O gráfico abaixo representa a evolução do preço das ações ao longo dos anos.
         """) #markdown

#Preparar as visualizações = filtros
st.sidebar.header("Filtros")

#Filtro de ações
lista_acoes = st.sidebar.multiselect("Escolha as ações para visualizar:",dados.columns)
if lista_acoes: 
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados= dados.rename(columns={acao_unica: "Close"})

#Filtro de datas
data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()
intervalo_data = st.sidebar.slider("Selecione o período:", min_value=data_inicial, max_value=data_final, value=(data_inicial,data_final), step=timedelta(days=1))   

dados = dados.loc[intervalo_data[0]:intervalo_data[1]] #Aqui ele filtra apenas o que o usuário selecionar

#Criar o gráfico
st.line_chart(dados)
