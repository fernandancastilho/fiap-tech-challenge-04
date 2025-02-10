import streamlit as st

# Configuração inicial do aplicativo
st.set_page_config(
    page_title="FIAP Pós Tech – Análise de Dados",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Conteúdo inicial da aplicação
st.markdown('<h2><span style="color:#FF0055;">FIAP</span> Pós Tech – Análise de Dados</h2>', unsafe_allow_html=True)
st.subheader("Dashboard Interativo para Análise de Dados e Modelagem Preditiva")

# Mensagem de boas-vindas
st.markdown("""
<div class="info-box">
    <p><strong>Bem-vindo ao Dashboard Interativo!</strong> Aqui você pode <strong>explorar dados</strong>, <strong>descobrir insights estratégicos</strong> e <strong>acessar modelos preditivos</strong> desenvolvidos pela turma <span style="color:#FF0055;">FIAP</span> Pós Tech.</p>
</div>
""", unsafe_allow_html=True)

# Seção "O que você encontrará"
# Seção "O que você encontrará"
st.markdown("""
 <br/>           
<h2 style="color:white; text-align:center;">📚 O que você encontrará neste Dashboard?</h2>

<div style="display: flex; flex-direction: column; gap: 10px;">
    <div style="background-color: #1e1e1e; padding: 20px; border-radius: 10px; border-left: 8px solid #FF0055;">
        <h6 style="color:#FF0055;">📊 Insights Estratégicos</h6>
        <p style="color:white; font-size: 16px;">Descubra informações valiosas sobre o mercado de petróleo, auxiliando na tomada de decisões estratégicas.</p>
    </div>
        <div style="background-color: #1e1e1e; padding: 20px; border-radius: 10px; border-left: 8px solid #FF0055;">
             <h6 style="color:#FF0055;">🤖 Previsões de Machine Learning</h6>
             <p style="color:white; font-size: 16px;">Acesse previsões precisas baseadas em modelos de Machine Learning, otimizando suas análises de mercado.</p>
        </div>
            <div style="background-color: #1e1e1e; padding: 20px; border-radius: 10px; border-left: 8px solid #FF0055;">
              <h6 style="color:#FF0055;">🖥️ Interatividade</h6>
              <p style="color:white; font-size: 16px;">Interaja com os dados por meio de filtros dinâmicos e gráficos personalizados no PowerBI, tornando a análise mais prática e envolvente.</p>
            </div>
</div>
""", unsafe_allow_html=True)
st.divider()
# Integrantes do grupo
st.write("##### 💻 Integrantes do Grupo")
st.write("**FIAP Pós Tech – Data Analytics, 2025. Grupo 13.**")

col1, col2 = st.columns(2)

with col1:
    st.write("- **Anderson Cardoso Pinto de Souza - RM: 357106**")
    st.write("- **Fernanda Nogueira Castilho - RM: 357000**")
    st.write("- **Jéssica da Silva Santos - RM: 356949**")

with col2:
    st.write("- **Nicholas Todescan Franco de Camargo - RM: 357423**")
    st.write("- **Wagner Silveira Santos - RM: 357110**")

if st.button("👉 Explore agora!"):
    st.write("Você pode começar navegando pelo menu lateral.")

# Rodapé estilizado
st.markdown("""
    <div style="text-align: center; margin-top: 30px; color: #999;">
        Criado pela turma <strong>6DTAT de Data Analytics</strong>, FIAP Pós Tech.
    </div>
""", unsafe_allow_html=True)

# CSS personalizado
st.markdown("""
    <style>
        .info-box {
            background-color: #333;
            border-left: 5px solid #FF0055;
            padding: 15px;
            border-radius: 8px;
            color: white;
        }

        h2, h3 {
            font-family: Arial, sans-serif;
        }

        .footer {
            font-size: 14px;
            margin-top: 20px;
            color: #999;
        }
    </style>
""", unsafe_allow_html=True)
