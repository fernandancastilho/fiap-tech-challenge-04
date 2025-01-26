import streamlit as st
import pandas as pd

# Configuração inicial do aplicativo
st.set_page_config(
    page_title="FIAP Pós Tech – Análise de Dados",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Conteúdo inicial da aplicação
st.title('Bem-vindo ao Dashboard Interativo!')

st.write(
    """
    Explore análises estratégicas e previsões inovadoras com base em modelos de Machine Learning.
    Navegue pelo menu lateral para acessar insights valiosos e descubra tendências no mercado de petróleo!
    """
)

# Adicionando um divisor estilizado
st.markdown("---")

# Seção: Sobre os integrantes
st.write("""### 💻 Integrantes do Grupo""")
st.write("**FIAP Pós Tech – Data Analytics, 2025. Grupo 13.**")

# Exibição dos integrantes com estilo adicional
data_integrantes = {
    "Nome": [
        "Anderson Cardoso Pinto de Souza",
        "Fernanda Nogueira Castilho",
        "Jéssica da Silva Santos",
        "Nicholas Todescan Franco de Camargo",
        "Wagner Silveira Santos",
    ],
    "Matrícula": ["123456", "123456", "123456", "123456", "123456"],
}
df_integrantes = pd.DataFrame(data_integrantes)

st.table(df_integrantes)

# Adicionando um rodapé estilizado
st.markdown(
    """
    <style>
    .footer {
        text-align: center;
        font-size: 14px;
        margin-top: 50px;
        color: #666;
        font-family: Arial, sans-serif;
    }
    </style>
    <div class="footer">
        Criado pela turma <strong>6DTAT de Data Analytics</strong>, FIAP Pós Tech.
    </div>
    """,
    unsafe_allow_html=True,
)