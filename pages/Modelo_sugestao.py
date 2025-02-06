import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
from datetime import date, timedelta
import yfinance as yf
from babel.dates import format_date

# CSS personalizado
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
    </style>
""", unsafe_allow_html=True)

st.markdown('<h2>📈 Previsão do Preço do Petróleo</h2>', unsafe_allow_html=True)

# Definir a data inicial como o dia atual
DATA_INICIAL = date.today()

# Texto explicativo com recomendação
data_inicial_formatada = format_date(DATA_INICIAL, format='long', locale='pt_BR')
st.markdown(f"""
<div class="st-info-box">
Defina a data desejada para prever o preço do barril de petróleo. Recomendamos previsões de curto prazo (<strong>7 a 15 dias</strong>) para maior precisão, mas você pode explorar até <strong>60 dias</strong> a partir de <strong>{data_inicial_formatada}</strong>.
</div><br/>
""", unsafe_allow_html=True)

# Entrada de dias futuros pelo usuário (limite de 7 a 60 dias)
diaspred = st.slider("Selecione o número de dias futuros:", min_value=7, max_value=60, value=15, step=1)

# Carregar dados
@st.cache_data
def load_data():
    df = yf.Ticker("BZ=F").history(period="max", interval="1d").reset_index()
    df['Date'] = pd.to_datetime(df['Date']).dt.tz_localize(None)
    df.rename(columns={'Close': 'Preço - petróleo bruto (Brent) - em dólares'}, inplace=True)
    df = df[['Date', 'Preço - petróleo bruto (Brent) - em dólares']].set_index('Date').dropna()
    return df

# Função para criar features temporais
def create_time_features(df):
    df['Ano'] = df.index.year
    df['Mês'] = df.index.month
    df['Dia'] = df.index.day
    df['Dia_Semana'] = df.index.weekday
    return df

# Função para calcular métricas
def calculate_metrics(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mape = mean_absolute_percentage_error(y_true, y_pred) * 100
    return mae, mse, rmse, mape

# Carregar e preparar os dados
df = load_data()
basef = create_time_features(df)
selected_features = ['Ano', 'Mês', 'Dia', 'Dia_Semana']
TARGET = "Preço - petróleo bruto (Brent) - em dólares"

if st.button("Prever"):
    # Divisão de treino e teste
    x_train, y_train = basef[selected_features], basef[TARGET]

    # Treinamento do modelo
    reg = xgb.XGBRegressor(objective="reg:squarederror", n_estimators=300, learning_rate=0.1)
    reg.fit(x_train, y_train)

    # Avaliação usando os últimos "diaspred" conhecidos
    last_n_days = basef.index[-diaspred:]  # Seleciona os últimos dias selecionados pelo usuário
    x_test, y_test = basef.loc[last_n_days, selected_features], basef.loc[last_n_days, TARGET]
    preds_test = reg.predict(x_test)

    # Calcular métricas
    mae, mse, rmse, mape = calculate_metrics(y_test, preds_test)

    # Criar datas futuras a partir do dia atual
    future_dates = pd.date_range(start=DATA_INICIAL + timedelta(days=1), periods=diaspred, freq='D')
    future_df = pd.DataFrame(index=future_dates)
    future_df = create_time_features(future_df)

    # Previsão para o período selecionado
    future_df['Previsão'] = reg.predict(future_df[selected_features])

    # Exibir métricas do modelo
    st.subheader(f"Métricas do Modelo (Últimos {diaspred} dias conhecidos)")
    st.write(f"**MAE:** {mae:.2f}")
    st.write(f"**MSE:** {mse:.2f}")
    st.write(f"**RMSE:** {rmse:.2f}")
    st.write(f"**MAPE:** {mape:.2f}%")

    # Exibir gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(basef.index[-30:], basef[TARGET].iloc[-30:], label='Preço Real (Brent)', color='green')
    ax.plot(future_df.index, future_df['Previsão'], linestyle='--', label='Previsão', color='blue')
    ax.set_title("Previsão do Preço do Petróleo (Brent)")
    ax.set_xlabel("Data")
    ax.set_ylabel("Preço (em dólares)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    # Exibir tabela de previsões
    st.subheader("Previsões Futuras")
    st.dataframe(future_df[['Previsão']].reset_index().rename(columns={'index': 'Data'}))
