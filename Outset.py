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
st.title('FIAP Pós Tech – Análise de Dados')
st.subheader("Dashboard Interativo para Análise de Dados e Modelagem Preditiva")

st.info("""Bem-vindo ao **Dashboard Interativo**! 🎯 Aqui você pode explorar dados, descobrir insights estratégicos e acessar modelos preditivos desenvolvidos pela turma FIAP Pós Tech.
        """)

# Contexto inicial com informações sobre o trabalho
st.markdown("""
---
📊 **O que você encontrará neste Dashboard?**
- **Insights estratégicos** sobre o mercado de petróleo.
- **Previsões baseadas em modelos de Machine Learning.**
- **Interatividade** para explorar os dados de forma prática e dinâmica.      
---
""")

st.write("##### 💻 Integrantes do Grupo")
st.write("**FIAP Pós Tech – Data Analytics, 2025. Grupo 13.**")

col1, col2 = st.columns(2)

with col1:
    st.write("- **Anderson Cardoso Pinto de Souza**")
    st.write("- **Fernanda Nogueira Castilho - RM: 357000**")
    st.write("- **Jéssica da Silva Santos**")

with col2:
    st.write("- **Nicholas Todescan Franco de Camargo**")
    st.write("- **Wagner Silveira Santos**")

if st.button("👉 Explore agora!"):
    st.write("Você pode começar navegando pelo menu lateral.")

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