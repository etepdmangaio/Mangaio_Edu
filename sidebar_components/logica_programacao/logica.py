import streamlit as st

def sidebar_logica_programacao():
    with st.sidebar.expander("📐 Lógica de Programação", expanded=False):
        return st.radio("Escolha uma trilha: ", [
            "O que é Lógica?",
            "Python",
            "Variáveis",
            "Estrutura de decisão",
            "Estrutura de controle"
        ], key="programacao_topico")
    


