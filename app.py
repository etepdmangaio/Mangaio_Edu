import streamlit as st
from sidebar_components.matematica.matematica import sidebar_matematica
from sidebar_components.geografia.geografia import sidebar_geografia
from sidebar_components.logica_programacao.logica import sidebar_logica_programacao
from sidebar_components.historia.historia_crise_primeiro_reinado import _crise_primeiro_reinado
from sidebar_components.historia.historia_deflagracao_revolta_1824 import _historia_deflagracao_revolta_1824
from sidebar_components.historia.historia_repressao_imperial import _historia_repressao_imperial
from sidebar_components.historia.historia_consequencias import _historia_consequencias

st.set_page_config(page_title="MangaioEdu", layout="wide")

st.sidebar.title("📚 Mangaio - Uma Plataforma Educacional Colaborativa")

with st.sidebar.expander("📖 História", expanded=False):
    # st.markdown("### Subtemas")
    subtema_escolhido = st.radio("Escolha uma trilha: ", [
        "Crise do Primeiro Reinado", "Insatisfação do Nordeste", "Influências Liberais e Republicanas",
        "Deflagração da Revolta (1824)", "Repressão Imperial", "Consequências"], key="subtema")
st.write("Subtema selecionado:", subtema_escolhido)

sidebar_geografia()

sidebar_matematica()

sidebar_logica_programacao()


if subtema_escolhido == "Crise do Primeiro Reinado":
    _crise_primeiro_reinado()

if subtema_escolhido == "Deflagração da Revolta (1824)":
    _historia_deflagracao_revolta_1824()

if subtema_escolhido == "Repressão Imperial":
    _historia_repressao_imperial()

if subtema_escolhido == "Consequências":
    _historia_consequencias()
