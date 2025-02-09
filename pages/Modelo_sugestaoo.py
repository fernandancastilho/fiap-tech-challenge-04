import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
import plotly.graph_objects as go
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
from datetime import date, timedelta
import yfinance as yf
from babel.dates import format_date

# Função para calcular métricas
def calculate_metrics(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mape = mean_absolute_percentage_error(y_true, y_pred) * 100
    return mae, mse, rmse, mape

# Cache para carregar e armazenar dados localmente
@st.cache_data
def load_data():
    df = yf.Ticker("BZ=F").history(period="2y", interval="1d").reset_index()  # Reduzir o período melhora o desempenho
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
    df['dia_anterior'] = df["Preço - petróleo bruto (Brent) - em dólares"].shift(1)  # Adiciona a feature do dia anterior
    return df.dropna()  # Remove valores NaN criados pelo shift

# Cache para treinar o modelo e reutilizá-lo
@st.cache_data
def train_model(x_train, y_train):
    reg = xgb.XGBRegressor(objective="reg:squarederror", n_estimators=300, learning_rate=0.1)
    reg.fit(x_train, y_train)
    return reg

# Carregar dados
df = load_data()
basef = create_time_features(df)

# Definir variáveis de interesse
TARGET = "Preço - petróleo bruto (Brent) - em dólares"
selected_features = ['Ano', 'Mês', 'Dia', 'Dia_Semana', 'dia_anterior']

# Divisão de dados de treino
x_train, y_train = basef[selected_features], basef[TARGET]
reg = train_model(x_train, y_train)  # Treinamento é feito apenas uma vez

# Interface do Streamlit
st.markdown('<h2>📈 Previsão do Preço do Petróleo</h2>', unsafe_allow_html=True)
diaspred = st.slider("Selecione o número de dias futuros:", min_value=1, max_value=30, value=7, step=1)

if st.button("Prever"):
    # Último preço de fechamento considerado
    ultimo_preco = basef[TARGET].iloc[-1]

    # Criar dados futuros
    future_dates = pd.date_range(start=date.today() + timedelta(days=1), periods=diaspred, freq='D')
    future_df = pd.DataFrame(index=future_dates)
    future_df['Ano'] = future_df.index.year
    future_df['Mês'] = future_df.index.month
    future_df['Dia'] = future_df.index.day
    future_df['Dia_Semana'] = future_df.index.weekday
    future_df['dia_anterior'] = [ultimo_preco] + [np.nan] * (len(future_df) - 1)
    future_df['dia_anterior'].ffill(inplace=True)  # Propagar o último valor conhecido

    # Fazer previsões
    future_df['Previsão'] = reg.predict(future_df[selected_features])

    # Calcular métricas com os dados reais mais recentes
    last_n_days = basef.index[-diaspred:]
    x_test, y_test = basef.loc[last_n_days, selected_features], basef.loc[last_n_days, TARGET]
    preds_test = reg.predict(x_test)
    mae, mse, rmse, mape = calculate_metrics(y_test, preds_test)

    # Exibir informações principais
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("###### 📉 Preço do Dia Anterior")
        st.write(f"**{ultimo_preco:.2f} USD**")
    with col2:
        st.markdown("###### 📊 Confiabilidade da Previsão")
        st.write(f"**{max(0, 100 - mape):.2f}%**")

    # Criar o gráfico
    df_plot = pd.DataFrame({
        'Data': list(basef.index[-30:]) + list(future_df.index),
        'Preço': list(basef[TARGET].iloc[-30:]) + list(future_df['Previsão']),
        'Tipo': ['Real'] * 30 + ['Previsão'] * len(future_df)
    })

    # Formatar as métricas para exibição no gráfico
    metricas_texto = f"MAE: {mae:.2f}, MSE: {mse:.2f}, RMSE: {rmse:.2f}, MAPE: {mape:.2f}%"
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_plot['Data'][:30], y=df_plot['Preço'][:30], mode='lines+markers', name='Dados Reais'))
    fig.add_trace(go.Scatter(x=df_plot['Data'][30:], y=df_plot['Preço'][30:], mode='lines+markers', name='Previsão'))
    fig.update_layout(
        title="Previsão do Preço do Petróleo (Brent)",
        xaxis_title="Data",
        yaxis_title="Preço (em dólares)",
        showlegend=True,
        annotations=[dict(xref="paper", yref="paper", x=0, y=1.15, text=metricas_texto, showarrow=False)]
    )

    st.plotly_chart(fig, use_container_width=True)

    # Exibir tabela de previsões
    st.subheader("Previsões Futuras")
    st.dataframe(future_df[['Previsão']].reset_index().rename(columns={'index': 'Data'}))
    st.success("✅ Previsão concluída com sucesso!")
