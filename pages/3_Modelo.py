#importar as bibliotecas
import streamlit as st
import pandas as pd 

st.set_page_config(
    page_title="Modelo",
    page_icon="⚙️",
    layout="wide",  # Configuração do layout (wide ou centered)
    initial_sidebar_state="expanded"  # Estado inicial da barra lateral
)

st.title("Modelo")