import streamlit as st

# Configurar o título da página e o ícone
st.set_page_config(
    page_title="Conclusão",  # Título da página
    page_icon="✅",  # Ícone da página
    layout="wide",  # Configuração do layout (wide ou centered)
    initial_sidebar_state="expanded"  # Estado inicial da barra lateral
)

# Estilização personalizada com uma linha sublinhada na cor da FIAP
def barra_titulo(titulo):
    st.markdown(f"""
    <h3 style="border-bottom: 3px solid #FF0055; padding-bottom: 10px;">{titulo}</h3>
    """, unsafe_allow_html=True)

barra_titulo("Conclusão")

#pula linha
st.markdown("""

""")

#Conteúdo da conclusão
st.markdown("""<h4>Petróleo</h4>
    <p style="text-align: justify;">
        &nbsp;&nbsp;&nbsp;&nbsp;O preço do petróleo é uma informação essencial para tomada de decisão de empresas que impactam bilhões de vidas diariamente. Seu uso se expande por toda a economia, não só para combustão de maquinários e meios de transporte de todas as escalas senão como matéria-prima para a produção de diversos insumos e produtos. Por isso, o acompanhamento diário de seu preço é notícia em qualquer país do globo e varia por consequência de diversos fatores.
        <br/><br/>
        &nbsp;&nbsp;&nbsp;&nbsp;O fator mais básico e fundamental para compreender seu preço é a relação entre oferta e demanda, sendo que desse vem todas as outras influências no seu cálculo. A demanda por petróleo é existente em todos os países, não só pelo seu uso como combustível, mas, por exemplo, a alta demanda por embalagens e outros produtos plásticos, presentes em qualquer economia. Já a oferta é um pouco mais complexa. O petróleo não é um insumo de fácil extração e sua qualidade é fundamental para seu uso, assim uma área reduzida do planeta detém uma concentração petrolífera muito grande. O mundo Árabe, por exemplo, tem grandes quantidades de jazidas e tem um poder enorme na mão, sendo a Arábia Saudita a terceira maior produtora do planeta. Mesmo sendo um país de proporções pequenas em comparação aos dois primeiros produtores, EUA e Rússia, produz quase a mesma quantidade de barris por anos que os dois.
        <br/><br/>
        &nbsp;&nbsp;&nbsp;&nbsp;Sendo a oferta e a demanda fatores fundamentais para a precificação do petróleo, qualquer fator que altere essas realidades gera grande impacto no preço do barril. A COVID-19, por exemplo, limitou fortemente a circulação de pessoas dentro e fora da fronteira de seus países, desestimulando o uso de combustível. A oferta não pôde acompanhar a redução pela urgência e surpresa, o que derrubou drasticamente o preço do barril, chegando a 9 dólares e 12 cents. Por outro lado, a Primavera Árabe, uma onda de protestos populares em diversos países do Oriente Médio que acabou por gerar grande instabilidade política na região, redução da oferta de petróleo e uma disparada no preço. O mesmo aconteceu mais recentemente (e ainda continua a acontecer) no conflito entre Rússia e Ucrânia. A Rússia, segunda maior produtora de petróleo no mundo, reduziu sua produção por gastos em outros setores para apoio à guerra, o que gerou aumento no preço do barril.
    </p>
""", unsafe_allow_html=True)

st.markdown("""<h4>Ações</h4>
    <p style="text-align: justify;">
        &nbsp;&nbsp;&nbsp;&nbsp;Tendo em vista a importância desses fatores para a precificação do petróleo, acompanhá-los é fundamental para previsões de precificações e suas flutuações para a tomada de decisão na precificação interna da gasolina e para projeções fundamentais ao negócio, como planejamento financeiro, fluxo de caixa, entre outras necessidades empresariais.
        <br/><br/>
        &nbsp;&nbsp;&nbsp;&nbsp;Para auxiliar no processo, desenvolvemos uma aplicação que pode prever o preço do petróleo utilizando-se de dados estatísticos históricos para que, com uma informação bem próxima da realidade futura, a empresa possa tomar decisões melhores de negócio. Utilizando-se desse modelo preditivo, a empresa pode definir o melhor preço médio do combustível e distribuí-lo de maneira eficiente por todas as regiões do país para maximizar seus lucros.
    </p>
""", unsafe_allow_html=True)

st.markdown("---")

# Rodapé estilizado
st.markdown("""
<div style="text-align: center; margin-top: 30px; color: #999;">
        Criado pela turma <strong>6DTAT de Data Analytics</strong>, FIAP Pós Tech.
    </div>
""", unsafe_allow_html=True) 
