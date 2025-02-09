import streamlit as st
import pandas as pd

# Configurar o título da página e o ícone
st.set_page_config(
    page_title="Exploração e Insights",  
    page_icon="📊",  
    layout="wide",  
    initial_sidebar_state="expanded"  
)

# Título principal da página
st.markdown("""<h2 class="main-title">📊 Exploração de Dados e Insights</h2>""", unsafe_allow_html=True)

# Análise geral e contextualização
st.subheader("🔍 Visão Geral: O que impulsiona os preços do petróleo?")

# Descrição introdutória
st.write("""
Nesta página, você encontrará uma análise interativa dos dados históricos do preço do petróleo Brent entre **2006** e **2025**. Com o apoio do **Power BI** desenvolvemos um dashboard dinâmico que revela insights fundamentais para entender as flutuações dos preços ao longo do tempo.

**Objetivo:** Explorar **quatro insights** principais que explicam os fatores que mais afetaram os preços e como eventos globais moldaram essas tendências.
""")

st.markdown("---")

# Insight 1
with st.expander("Insight 1: 🌍 Histórico e grandes crises (longo prazo e tendências de mercado)"):
    st.markdown("""
    ### **Contexto**
    Entre 2006 e 2025, o mercado de petróleo enfrentou diversas flutuações de preço, impulsionadas por fatores econômicos, políticos e de oferta. Durante este período, observamos que momentos de crise desempenharam um papel significativo na elevação dos preços médios, ao mesmo tempo em que períodos de recuperação contribuíram para estabilizações ou quedas.

    """)

    st.image("analise_petroleo_media_preco_por_ano.jpg", caption="Dashboard de Preço Médio do Petróleo por Ano",  use_container_width=True)
    
    st.markdown("""
    ### **Descoberta Principal**
    Ao analisarmos os dados do dashboard, identificamos que os anos com maiores elevações no preço médio do petróleo estão diretamente relacionados a eventos críticos.
    """)

    st.markdown("""
    ### **Fatores-Chave Identificados**
    - **Crise Subprime (2008):** Iniciada no mercado imobiliário dos EUA, essa crise global gerou instabilidade econômica mundial, afetando o consumo de energia e causando volatilidade nos preços de commodities.
    
    - **Primavera Árabe (2011-2012):** A instabilidade geopolítica no Oriente Médio, região estratégica para a produção global de petróleo, desencadeou interrupções na oferta e impulsionou os preços.
    
    - **Crise Econômica de 2014:** A desaceleração global e políticas econômicas desfavoráveis na China e Europa reduziram a demanda por petróleo. O excesso de oferta intensificou a queda nos preços, resultando em uma das maiores desvalorizações do período.

    - **COVID-19 (2020):** A pandemia resultou em uma queda drástica na demanda global por petróleo, especialmente no setor de transporte e indústrias. Isso causou um acúmulo de estoques e queda nos preços, com o menor preço médio do período registrado em **9,12 USD/barril**.
         
    - **Guerra da Rússia e Crise Energética (2022):** Com a invasão da Ucrânia, houve um choque no fornecimento global de petróleo, resultando no maior preço médio desde 2008.
    """)

   
    st.markdown("""

    """)

    # Métricas específicas
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Maior Preço Registrado", value="143,95 USD/barril", delta="📈 durante Primavera Árabe")
    col2.metric(label="Preço Médio", value="77,62 USD/barril")
    col3.metric(label="Menor Preço", value="9,12 USD/barril", delta="📉 na COVID-19")

    st.markdown("""
    ### **Conclusão**
    Este insight destaca a importância de monitorar eventos geopolíticos como um fator determinante para a previsão de preços futuros. Entender o histórico de crises passadas pode fornecer uma base sólida para antecipar movimentos no mercado de petróleo, especialmente em períodos de incerteza global.
    """)


# Insight 2
with st.expander("Insight 2: 📈 Impacto imediato de eventos geopolíticos (disparada de preços)"):
    st.markdown("""
    ### **Contexto**
    O preço do petróleo é extremamente sensível a eventos externos e internos, e nossa análise revelou que os maiores aumentos no preço médio estão associados a crises geopolíticas, instabilidade regional e decisões estratégicas de grandes players, como a Organização dos Países Exportadores de Petróleo (OPEP). Esses eventos atuam como catalisadores, criando desequilíbrios na oferta e na demanda, o que resulta em picos nos preços.
    """)

    st.image("analise_petroleo_influencia_aumento_preco.jpg", caption="Influência no Aumento do Preço do Petróleo",use_container_width=True)

    st.markdown("""
    ### **Descoberta Principal**
    O evento com maior influência no aumento do preço médio foi a **Primavera Árabe (2011-2012)**, com um aumento médio de 35,75 USD/barril. Esse período foi marcado por forte instabilidade no Oriente Médio, resultando na interrupção da produção em diversos países-chave. Outros eventos, como as decisões estratégicas da **OPEP** e a **Guerra da Rússia e Crise Energética**, também tiveram um impacto significativo no aumento dos preços.
  """)

    st.markdown("""
    ### **Fatores-Chave Identificados**
    - **Primavera Árabe (2011-2012) - +35,75 USD/barril:** A instabilidade política e social no Oriente Médio, região responsável por grande parte da produção global, gerou uma crise de oferta, elevando os preços rapidamente.
 
    - **OPEP (2013) - +32,84 USD/barril:** As decisões da OPEP de limitar a produção foram fundamentais para sustentar os preços, especialmente em um cenário de alta demanda global.

    - **Guerra da Rússia e Crise Energética (2022) - +24,26 USD/barril:** A invasão russa na Ucrânia afetou diretamente o fornecimento de petróleo na Europa, levando a uma corrida por fontes alternativas de energia e pressionando os preços para cima.

    - **Fatores externos diversos (entre 2006 e 2015) - +16,01 USD/barril:** Eventos como sanções econômicas e tensões em áreas produtoras criaram desequilíbrios que influenciaram aumentos moderados.

    - **Crise Subprime (2008) - +8,18 USD/barril:** Embora tenha resultado em quedas subsequentes, os efeitos iniciais da crise geraram picos nos preços devido à volatilidade e incertezas no mercado.
    """)

    st.markdown("""

    """)

    col1, col2 = st.columns(2)
    col1.metric(label="Aumento Médio em Crises", value="+27,5 USD/barril")
    col2.metric(label="Queda Pós-Crise (2015)", value="-22,3%")

    st.markdown("""
    ### **Conclusão**
    Esse insight reforça a importância de monitorar tanto crises geopolíticas quanto as decisões estratégicas de grandes players para entender os movimentos futuros no mercado de petróleo. A combinação de fatores externos e internos pode criar ciclos de alta sustentados, como observamos durante os eventos analisados.
    """)

# Insight 3
with st.expander("Insight 3: 📉 Quedas abruptas devido a choques econômicos e pandemias (redução da demanda)"):

    # Contexto
    st.markdown("""
    ### **Contexto**
    Enquanto fatores como crises geopolíticas e restrições de oferta elevam o preço do petróleo, a análise mostrou que eventos econômicos e crises sanitárias podem criar cenários de queda acentuada nos preços. Essas quedas ocorrem, principalmente, quando há redução drástica na demanda global, seja devido a recessões econômicas ou paralisações generalizadas, como observado durante a pandemia da COVID-19.    
    """)
 
    st.image("analise_petroleo_influencia_diminuicao_preco.jpg", caption="Influência na Diminuição do Preço do Petróleo",use_container_width=True)

    # Descoberta principal
    st.markdown("""
    ### **Descoberta Principal**
    O evento que mais influenciou a redução no preço médio do petróleo foi a **Crise causada pela COVID-19 (2020-2021)**, resultando em uma queda média de 23,35 USD/barril. Durante esse período, medidas de isolamento social e interrupções em setores como transporte e indústria levaram a uma forte redução na demanda global por petróleo. Outros fatores, como a **Crise Econômica de 2014**, também foram responsáveis por quedas significativas.
    """)

    # Fatores-Chave Identificados
    st.markdown("""
    ### **Fatores-Chave Identificados**
    - **Crise causada pela COVID-19,  -23,35 USD/barril:** A pandemia provocou a maior queda recente no preço do petróleo devido à desaceleração global e à queda na demanda por transporte e produção industrial. O acúmulo de estoques também pressionou os preços para baixo.

    - **Crise Econômica de 2014,  -15,31 USD/barril:** A combinação de uma oferta elevada e a desaceleração econômica global, especialmente em países emergentes, levou a um excesso de petróleo no mercado e a quedas acentuadas nos preços.

    - **Fatores internos e externos (2015-2020) - -14,5 USD/barril:** Decisões internas relacionadas à produção excessiva, aliadas a contextos externos, contribuíram para quedas moderadas e prolongadas no preço do petróleo.

    - **Outros fatores (Em branco),  -5,84 USD/barril:** Embora menores, fatores adicionais não especificados no gráfico também contribuíram para quedas sazonais, possivelmente relacionadas a ciclos de oferta e demanda.
    """)

    st.markdown("""

    """)

    # Métricas específicas
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Queda Média Durante a COVID-19", value="-23,35 USD/barril")
    col2.metric(label="Maior Preço Pré-COVID", value="143,95 USD/barril")
    col3.metric(label="Queda Acumulada (2014-2020)", value="-15,31 USD/barril")

    st.markdown("""
    ### **Conclusão**
    Esse insight revela que monitorar crises econômicas e sanitárias globais é fundamental para prever quedas acentuadas no preço do petróleo. Entender os fatores internos e externos pode ajudar a antecipar períodos de baixa no mercado e fornecer estratégias adequadas para mitigação de riscos.
    """)

# Insight 4
with st.expander("Insight 4: 🛢️ Primavera Árabe: Um evento regional com impacto global"):

    # Contexto
    st.markdown("""
    ### **Contexto**
    A Primavera Árabe, ocorrida entre 2011 e 2012, foi um período de forte instabilidade política em diversos países do Oriente Médio e Norte da África, uma região responsável por uma grande parcela da produção global de petróleo. Com a eclosão de conflitos, especialmente na Líbia, houve uma drástica redução na oferta de petróleo, criando um cenário de alta volatilidade nos preços.
    """)
 
    st.image("analise_petroleo_media_preco_primavera_arabe.jpg", caption="Média de Preço durante a Primavera Árabe", use_container_width=True)

    # Descoberta principal
    st.markdown("""
    ### **Descoberta Principal**
    Durante o período da Primavera Árabe, o preço médio do petróleo saltou de **77,62 USD/barril** (antes da crise) para **111,50 USD/barril**, representando um aumento de **+43,6%**. A guerra civil na Líbia, que interrompeu grande parte da produção do país, foi um dos fatores centrais para essa elevação. Ao mesmo tempo, o menor preço observado no período subiu drasticamente de **9,12 USD/barril** para **88,69 USD/barril**, uma alta de impressionantes **+872%**.
    """)

    # Fatores-Chave Identificados
    st.markdown("""
    ### **Fatores-Chave Identificados**
    - **Interrupção da Produção na Líbia:** A guerra civil reduziu significativamente a oferta de petróleo no mercado global, afetando as exportações do país e pressionando os preços.

    - **Incertezas Políticas Regionais:** A instabilidade em outros países, como Egito, Tunísia e Síria, criou um ambiente de risco, onde os investidores passaram a precificar prêmios de risco no petróleo, elevando os preços.

    - **Dependência Global do Oriente Médio:** Com boa parte do suprimento global vindo dessa região, qualquer interrupção na produção afeta diretamente o equilíbrio da oferta e demanda.
    """)

    st.markdown("""

    """)

    # Métricas específicas
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Maior Preço", value="128,14 USD/barril")
    col2.metric(label="Preço Médio", value="111,50 USD/barril")
    col3.metric(label="Menor Preço", value="88,69 USD/barril")

    # Conclusão
    st.markdown("""
    ### **Conclusão**
    Este insight reforça que, em períodos de conflitos geopolíticos intensos, os mercados de commodities reagem não apenas aos choques imediatos de oferta, mas também ao aumento da percepção de risco. A Primavera Árabe é um exemplo claro de como instabilidades políticas podem provocar aumentos sustentados nos preços do petróleo, e monitorar esse tipo de evento é fundamental para prever oscilações futuras.
    """)

# Linha de separação
st.markdown("---")

# Conclusão geral
st.markdown("<h3> ✅ Conclusão </h3>", unsafe_allow_html=True)

st.write("""
Durante a nossa análise, descobrimos que fatores como crises econômicas e geopolíticas influenciam diretamente os preços do petróleo. Esses eventos criam padrões que, quando observados ao longo do tempo, nos ajudam a entender e prever as oscilações do mercado. 

Com base nesses aprendizados, desenvolvemos um modelo preditivo que utiliza dados históricos e tendências globais para fornecer previsões claras e confiáveis, facilitando decisões estratégicas.
""")

# Linha de separação
st.markdown("---")

# Próximos passos
st.markdown("<h3>O que vem a seguir?</h3>", unsafe_allow_html=True)
st.markdown("""
O modelo preditivo desenvolvido utiliza algoritmos como o **XGBoost** para integrar fatores históricos e geopolíticos nas previsões diárias. Isso permite identificar padrões cíclicos e eventos inesperados, aprimorando a tomada de decisão em cenários de alta volatilidade.
""")


# Link para navegação
st.markdown("""
    <div style="font-size:18px;">
    👉 <a href="/Modelo" target="_self" style="text-decoration: none; color: #1f77b4;">
    Clique aqui para acessar a previsão de preços
    </a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Referências
st.markdown("<h3>📚 Referências</h3>", unsafe_allow_html=True)

references = {
    "Base de Dados IPEA": "https://www.ipea.gov.br",
    "Documentação do XGBoost": "https://xgboost.readthedocs.io",
    "Documentação do Streamlit": "https://docs.streamlit.io",
    "Power BI": "https://powerbi.microsoft.com"
}

# Exibir as referências como uma lista interativa
for name, link in references.items():
    st.markdown(f"- 🌐 [**{name}**]({link})")

# Rodapé estilizado
st.markdown("""
<div style="text-align: center; margin-top: 30px; color: #999;">
        Criado pela turma <strong>6DTAT de Data Analytics</strong>, FIAP Pós Tech.
    </div>
""", unsafe_allow_html=True)
