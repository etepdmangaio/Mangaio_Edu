import streamlit as st

def sidebar_geografia():
    with st.sidebar.expander("🌍 Geografia", expanded=False):
        return st.radio("Escolha uma trilha:", [
            "Climas do Brasil",
            "Relevo",
            "Urbanização",
            "Cartografia"
        ], key="geografia_topico")


