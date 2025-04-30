import streamlit as st

#ainda com array
def verificar_login(usuario, senha):
    usuarios = {
        "admin": "admin123",
        "usuario": "senha123"
    }
    if usuario in usuarios and usuarios[usuario] == senha:
        return True
    return False


def pagina_login():
    st.title("MangaioEdu")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Login"):
        if verificar_login(usuario, senha):
            st.session_state["logado"] = True
            st.session_state["usuario"] = usuario
            st.success("Login realizado com sucesso!")
        else:
            st.error("Usuário ou senha incorretos.")




#Não implementado
def pagina_principal():
    st.title(f"Bem-vindo, {st.session_state['usuario']}!")
    st.write("Esta é a página principal.")

    
    st.write("### Funcionalidades:")
    st.button("Botão 1")
    st.button("Botão 2")

    # Botão de logout
    if st.button("Logout"):
        st.session_state["logado"] = False
        st.session_state["usuario"] = None
        st.experimental_rerun()  # Recarrega a página para voltar ao login

# Configuração inicial do estado de sessão
if "logado" not in st.session_state:
    st.session_state["logado"] = False
if "usuario" not in st.session_state:
    st.session_state["usuario"] = None

# Controle de exibição das páginas
if st.session_state["logado"]:
    pagina_principal()
else:
    pagina_login()