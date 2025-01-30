import streamlit as st
from datetime import date, timedelta
import locale

# Configuração de idioma para a data
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

# Configurações do Streamlit
st.set_page_config(page_title="Deploy | Tech Challenge 4 | FIAP", layout='wide')

# CSS personalizado para botões, rótulos e elementos
st.markdown("""
    <style>
        h2 {
            color: #FF0055;
            font-size: 28px;
        }
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
        .stButton>button:hover {
            background-color: #e6004c;
        }
        .stDateInput>div {
            background-color: #333;
            border: 2px solid #FF0055;
            border-radius: 5px;
        }
        .stDateInput input {
            color: white;
        }
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

# Título estilizado
st.markdown('<h2>📈 Previsão do Preço do Petróleo</h2>', unsafe_allow_html=True)

# Definir a data inicial e o limite de dias para a previsão
DATA_INICIAL = date(2025, 1, 30)
LIMITE_DIAS = 15

# Formatando a data inicial para exibição na mensagem
data_inicial_formatada = DATA_INICIAL.strftime("%d de %B de %Y")

# Caixa de informações
st.markdown(f"""
<div class="st-info-box">
Defina a data desejada para prever o preço do barril de petróleo. Você pode selecionar até <strong>15 dias</strong> após <strong>{data_inicial_formatada}</strong>. Com dados atualizados, oferecemos previsões precisas e insights rápidos para apoiar suas melhores decisões.
</div>
<br/>
""", unsafe_allow_html=True)

# Entrada de data pelo usuário
with st.container():
    st.write("**Escolha a data de previsão:**")
    col1, _ = st.columns([2, 5])
    with col1:
        min_date = DATA_INICIAL + timedelta(days=1)
        max_date = DATA_INICIAL + timedelta(days=LIMITE_DIAS)
        end_date = st.date_input(
            "", 
            min_value=min_date, 
            max_value=max_date,
            value=min_date
        )

# Calcular o número de dias para a previsão com base na data selecionada
days = (end_date - DATA_INICIAL).days

# Botão estilizado
if st.button('Prever'):
    st.success(f"✅ Previsão concluída para **{end_date.strftime('%d de %B de %Y')}**!")
