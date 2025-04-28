import streamlit as st

def sidebar_matematica():
    with st.sidebar.expander("📐 Matemática", expanded=False):
        return st.radio("Escolha uma trilha", [
            "Álgebra",
            "Geometria",
            "Probabilidade"
        ], key="matematica_topico")
