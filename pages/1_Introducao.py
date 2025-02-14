import streamlit as st

# Configurar o título da página e o ícone
st.set_page_config(
    page_title="Tech Challenge: Mercado de Petróleo",  # Título da página
    page_icon="💻",  # Ícone da página
    layout="wide",  # Configuração do layout (wide ou centered)
    initial_sidebar_state="expanded"  # Estado inicial da barra lateral
)

# Estilização personalizada com uma linha sublinhada na cor da FIAP
def barra_titulo(titulo):
    st.markdown(f"""
    <h3 style="border-bottom: 3px solid #FF0055; padding-bottom: 10px;">{titulo}</h3>
    """, unsafe_allow_html=True)

# Corpo da página inicial 
st.title("Tech Challenge: Análise do Mercado de Petróleo")
st.write("Uma abordagem integrada para análise de dados históricos e previsão de tendências no setor energético.")

# Funções para cada aba
def introducao():
    barra_titulo("Introdução")
    st.markdown("""

""")
    st.write("""
O mercado global de petróleo tem um impacto fundamental na economia mundial, influenciando a maior parte dos setores econômicos, desde a produção de combustível até cadeias de produção industrial, sendo por exemplo a matéria-prima da produção do plástico. As variações no preço do petróleo Brent, uma das principais referências globais, resultam de fatores geopolíticos, econômicos e mudanças na demanda por energia e influencia fortemente as relações comerciais entre diversos países.

No período de **2006** a **2025**, esses preços foram formados por importantes eventos pelo mundo, tais como crises financeiras, pandemias e conflitos internacionais, demonstrando a necessidade de uma análise criteriosa visando previsões precisas para subsidiar tomadas de decisão estratégicas no que se refere à produção e precificação do insumo em território nacional, principalmente o combustível.

Este trabalho desenvolve um dashboard interativo e um modelo preditivo para estimar os preços futuros do petróleo, utilizando dados históricos e técnicas de aprendizado de máquina. A aplicação foi implementada no **Streamlit**, proporcionando aos usuários uma experiência interativa e prática.
""")
    st.image("img_IA.png", caption="Fonte: Imagem gerada por IA (DALL·E 3)", use_container_width=True)

def objetivo():
    barra_titulo("Objetivos do Estudo")
    st.markdown("""

""")
    st.write("""
O objetivo central deste estudo é apresentar uma solução integrada de análise e previsão dos preços do petróleo Brent, com foco em previsões a curto e médio prazo, por meio das seguintes utilidades esperadas:

1. **Dashboard no Power BI:** Apresentar insights relevantes sobre as oscilações nos preços do petróleo, destacando fatores geopolíticos e econômicos.

2. **Modelo preditivo:** Desenvolver um modelo robusto de aprendizado de máquina (XGBoost) para prever os preços futuros.

3. **Apoio à tomada de decisão:** Fornecer informações estratégicas e acionáveis para subsidiar decisões corporativas, reduzindo os riscos associados à volatilidade do mercado.
""")

def metodologia():
    barra_titulo("Metodologia")
    st.markdown("""

""")
    st.write("""
A metodologia utilizada neste estudo foi dividida em quatro etapas fundamentais, descritas a seguir:
""")

    st.markdown("#### 1. Coleta e Pré-processamento dos Dados")
    st.write("""
Os dados históricos do preço do petróleo Brent foram obtidos através do site do **Instituto de Pesquisa Econômica Aplicada (IPEA)** e da **API do Yahoo Finance**, abrangendo um período de 20 anos. No pré-processamento, foram geradas variáveis temporais como ano, mês e dia, além da inclusão do preço do dia anterior como uma feature relevante para a análise sazonal.
""")

    st.markdown("#### 2. Análise Exploratória e Identificação de Padrões")
    st.write("""
A análise exploratória foi realizada através de um dashboard no Power BI, permitindo a visualização das principais tendências e fatores externos que influenciam os preços do petróleo. Os resultados foram utilizados para selecionar as variáveis mais significativas para o modelo preditivo.
""")

    st.markdown("#### 3. Construção e Treinamento do Modelo Preditivo")
    st.write("""
O modelo preditivo foi construído utilizando o algoritmo **XGBoost** (Extreme Gradient Boosting), uma abordagem eficaz para lidar com dados não lineares e voláteis. As etapas de modelagem incluíram:

- **Divisão do conjunto de dados:** 80% dos dados foram utilizados para treinamento e 20% para validação.
- **Seleção de variáveis:** Variáveis temporais e o preço do dia anterior foram incluídos como preditores.
- **Avaliação de desempenho:** O modelo foi avaliado por meio das métricas **MAE**, **RMSE** e **MAPE**, visando a minimização do erro.
""")

    st.markdown("#### 4. Implementação da Aplicação Interativa no Streamlit")
    st.write("""
A aplicação final foi implementada no **Streamlit**, oferecendo uma interface interativa que permite aos usuários selecionar o período de previsão e visualizar os resultados de forma dinâmica. As principais funcionalidades incluem:

- **Previsão a curto e médio prazo:** Intervalo de 7 a 30 dias.
- **Visualização de preços reais e previstos:** Gráficos interativos destacando a comparação entre os dados históricos e as previsões.
- **Transparência nas métricas de desempenho:** Apresentação das métricas utilizadas e justificativa para a escolha do modelo.
""")

# Menu de abas sem ícones para um tom mais formal
tabs = st.tabs(["Introdução", "Objetivos", "Metodologia"])

# Adicionando conteúdo às abas
with tabs[0]: 
    introducao()
with tabs[1]:  
    objetivo()
with tabs[2]:  
    metodologia()

st.markdown("---")

# Rodapé estilizado
st.markdown("""
<div style="text-align: center; margin-top: 30px; color: #999;">
        Criado pela turma <strong>6DTAT de Data Analytics</strong>, FIAP Pós Tech.
    </div>
""", unsafe_allow_html=True) 
