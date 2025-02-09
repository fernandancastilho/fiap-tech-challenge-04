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
Defina a data desejada para prever o preço do barril de petróleo. O modelo se baseia no fechamento do dia anterior para calcular as previsões futuras.
Recomendamos previsões de curto prazo (<strong>7 a 15 dias</strong>) para maior precisão, mas você pode explorar até <strong>30 dias</strong> a partir de <strong>{data_inicial_formatada}</strong>.
</div><br/>
""", unsafe_allow_html=True)

# Entrada de dias futuros pelo usuário (limite de 1 a 30 dias)
diaspred = st.slider("Selecione o número de dias futuros:", min_value=1, max_value=30, value=7, step=1)

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

# Criar a nova feature dia_anterior
def create_lag_features(df):
    df['dia_anterior'] = df[TARGET].shift(1)  # Cria a coluna dia_anterior com o preço do dia anterior
    return df.dropna()  # Remove linhas iniciais com valores NaN gerados pelo shift()

# Carregar e preparar os dados
df = load_data()
basef = create_time_features(df)
TARGET = "Preço - petróleo bruto (Brent) - em dólares"
basef = create_lag_features(basef)  # Adicionar dia_anterior

selected_features = ['Ano', 'Mês', 'Dia', 'Dia_Semana', 'dia_anterior']  # Incluindo dia_anterior

if st.button("Prever"):
    with st.spinner("🔄 Treinando o modelo e gerando a previsão... Isso pode levar até 5 minutos."):
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

        # Último preço de fechamento considerado
        ultimo_preco = basef[TARGET].iloc[-1]

        # Cálculo de confiabilidade (100% - MAPE)
        confiabilidade = max(0, 100 - mape)

        # **Mostrar informações em duas colunas lado a lado**
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("###### 📉 Preço do Dia Anterior")
            st.write(f"**{ultimo_preco:.2f} USD**")
        with col2:
            st.markdown("###### 📊 Confiabilidade da Previsão")
            st.write(f"**{confiabilidade:.2f}%**")

        # Criar previsões futuras
        future_dates = pd.date_range(start=DATA_INICIAL + timedelta(days=1), periods=diaspred, freq='D')
        future_df = pd.DataFrame(index=future_dates)
        future_df = create_time_features(future_df)
        future_df['dia_anterior'] = [ultimo_preco] + [np.nan] * (len(future_df) - 1)
        future_df['dia_anterior'] = future_df['dia_anterior'].ffill()
        future_df['Previsão'] = reg.predict(future_df[selected_features])

        # Criar gráfico
        df_plot = pd.DataFrame({
            'Data': list(basef.index[-30:]) + list(future_df.index),
            'Preço': list(basef[TARGET].iloc[-30:]) + list(future_df['Previsão']),
            'Tipo': ['Real'] * 30 + ['Previsão'] * len(future_df)
        })

        metricas_texto = f"MAE: {mae:.4f}, MSE: {mse:.4f}, RMSE: {rmse:.4f}, MAPE: {mape:.2f}%"
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_plot['Data'][:30], y=df_plot['Preço'][:30], mode='lines+markers', name='Dados Reais'))
        fig.add_trace(go.Scatter(x=df_plot['Data'][30:], y=df_plot['Preço'][30:], mode='lines+markers', name='Previsão'))
        fig.update_layout(
            title="Previsão do Preço do Petróleo (Brent)",
            xaxis_title="Data",
            yaxis_title="Preço (em dólares)",
            showlegend=True,
            plot_bgcolor="black",
            paper_bgcolor="black",
            font=dict(color="white"),
            annotations=[dict(xref="paper", yref="paper", x=0, y=1.15, text=metricas_texto, showarrow=False)]
        )

        st.plotly_chart(fig, use_container_width=True)

        # Explicação das métricas em um expander
        with st.expander("📋 Explicação das Métricas"):
            st.write("""
            - **MAE (Mean Absolute Error):** Indica a média dos erros absolutos entre os valores reais e previstos. Um valor menor indica maior precisão.
            - **MSE (Mean Squared Error):** Mede a média dos erros ao quadrado. Penaliza erros maiores mais fortemente.
            - **RMSE (Root Mean Squared Error):** A raiz quadrada do MSE, o que facilita a interpretação, mantendo as unidades originais.
            - **MAPE (Mean Absolute Percentage Error):** Mostra a porcentagem média de erro absoluto em relação aos valores reais. Idealmente, deve ser baixo.
            """)

        st.subheader("Previsões Futuras")
        st.dataframe(future_df[['Previsão']].reset_index().rename(columns={'index': 'Data'}))
        st.success("✅ Previsão concluída com sucesso!")
