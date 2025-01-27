# streamlit: name="Página Inicial"
import streamlit as st
import pandas as pd 

# Configurar o título da página e o ícone
st.set_page_config(
    page_title="Tech Challenge: Mercado de Petróleo",  # Título da página
    page_icon="💻",  # Ícone da página
    layout="wide",  # Configuração do layout (wide ou centered)
    initial_sidebar_state="expanded"  # Estado inicial da barra lateral
)

#Menu lateral   
st.sidebar.header("FIAP Pós Tech – Data Analytics")

st.sidebar.info("Criado pela turma **6DTAT de Data Analytics**, FIAP Pós Tech.") 

#Corpo da página inicial 
st.title("  Análise do Mercado de Petróleo")
st.write("Uma solução analítica para entender o mercado energético e prever tendências com base em dados históricos.")

# Funções para cada aba
def introducao():
    st.write("""### Explorando Tendências no Mercado de Petróleo""")
    st.write("""O mercado global de petróleo está entre os mais dinâmicos e imprevisíveis do mundo, sendo influenciado por fatores geopolíticos, crises econômicas e variações na demanda por energia. Essas flutuações impactam diretamente empresas, investidores e governos, exigindo ferramentas analíticas e preditivas para compreender o cenário e tomar decisões estratégicas.
    
Neste contexto, o **Tech Challenge** apresenta-se como uma oportunidade prática para aplicar conhecimentos técnicos e explorar como a análise de dados e o aprendizado de máquina podem oferecer insights sobre a evolução do preço do petróleo. O desafio inclui o desenvolvimento de um dashboard interativo e de um modelo preditivo que projete as oscilações diárias do preço do petróleo, com base em dados históricos, permitindo uma visão estratégica e fundamentada.
    """)
    st.image("img_IA.png", caption="Fonte: Imagem gerada por IA (DALL·E 3)", use_container_width=True)

def objetivo():
    st.write("### Objetivo")
    st.write("""O projeto tem como objetivo desenvolver uma solução analítica integrada que combine storytelling, tecnologia e análise de dados, visando otimizar a previsão e a compreensão dos preços do petróleo e, assim, apoiar a tomada de decisão estratégica no setor. Para atingir esse objetivo, o trabalho contempla três ações principais que se complementam:
#### 📊 Dashboard no Power BI
Criação de um dashboard interativo no Power BI, permitindo a visualização de insights detalhados sobre os fatores que influenciam a variação dos preços do petróleo. Esses fatores incluem eventos geopolíticos, crises econômicas e oscilações na demanda energética global, sendo apresentados de forma clara e dinâmica para facilitar a interpretação dos usuários.
#### 🤖 Modelo preditivo
Desenvolvimento de um modelo preditivo baseado em séries temporais, utilizando técnicas de Machine Learning, com o intuito de prever os preços futuros do petróleo e avaliar a performance de diferentes algoritmos.
#### 🖥️ Interface interativa
Estruturação de um plano de implementação que disponibilize o modelo preditivo em uma interface interativa e acessível, utilizando ferramentas modernas como o Streamlit. Essa etapa possibilita que os usuários explorem as previsões de forma intuitiva, promovendo maior integração entre o modelo e a aplicação prática no ambiente de negócios.

Com a integração dessas ações, o trabalho visa oferecer uma solução completa, prática e eficaz, que transforme dados complexos em informações estratégicas e acionáveis, fomentando análises preditivas de alta qualidade no mercado de petróleo.
        """)

def metodologia():
    st.write("### Metodologia")
    st.write("""O desenvolvimento deste projeto seguiu uma abordagem estruturada, com etapas bem definidas que garantiram o alinhamento entre as ações realizadas e os objetivos propostos.

Inicialmente, foi realizada a **coleta de dados**, na qual a base histórica de preços do petróleo foi extraída do site do IPEA. A base, composta pelas colunas de data e preço em dólares, foi complementada com dados adicionais relevantes, como eventos geopolíticos, crises econômicas e variações na demanda energética global. Essa integração de dados proporcionou uma visão mais ampla dos fatores que influenciam o mercado.

Na etapa de **análise exploratória**, os dados foram processados para identificar padrões, tendências sazonais e correlações significativas. Foram aplicadas técnicas de visualização de dados e análise estatística, o que possibilitou compreender melhor as oscilações nos preços do petróleo e embasar os insights apresentados posteriormente.

Com base nas informações obtidas, foi desenvolvido um dashboard interativo utilizando o Power BI. Este dashboard destaca os fatores que influenciam a variação do preço do petróleo, organizados em narrativas visuais claras e objetivas. Quatro insights principais foram apresentados, abordando o impacto de situações geopolíticas, crises econômicas, demanda global por energia e inovações tecnológicas.  

Para a etapa de **modelagem preditiva**, diversos modelos de Machine Learning foram explorados, incluindo Prophet e LSTM. Após testes e validações, foi selecionado o modelo com melhor desempenho, considerando métricas como MAE, RMSE e MAPE. Este modelo foi utilizado para prever o preço diário do petróleo, oferecendo uma ferramenta confiável para tomada de decisão.

Por fim, foi implementado o **deploy do MVP** utilizando a ferramenta Streamlit. A interface criada permite acesso simplificado ao modelo preditivo, garantindo que os resultados sejam acessíveis e práticos para os usuários finais.

Este processo metodológico integrou análise de dados, ferramentas tecnológicas e comunicação visual para entregar uma solução robusta e estratégica, oferecendo insights relevantes e previsões confiáveis sobre o comportamento do mercado de petróleo.
        """)


#Menu tabs 
tabs = st.tabs (['Introdução', 'Objetivo', 'Metodologia'])

# Aba "Introdução"
with tabs[0]: 
    introducao()
# Aba "Objetivo"
with tabs[1]:  
    objetivo()

# Aba "Metodologia"
with tabs[2]:  
    metodologia()