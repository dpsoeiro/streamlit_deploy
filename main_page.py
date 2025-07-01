import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime 
from helper import Helper

st.set_page_config(
    page_title="Principal",
    page_icon="🏃🏼",
    layout="wide"
)


helper = Helper()

### variaveis

arquivo_config = helper.open_yaml()
logo_futcode = arquivo_config['logo_principal']


if "data" not in st.session_state:

    st.session_state["data"] = helper.load_main_file()


st.header("SISTEMA :blue[FUTCODE] DE MONITORAMENTO E RECOMENDAÇÃO DE ATLETAS! ⚽️", width = "stretch" )


# Inserir imagem na sidebar
st.sidebar.image(logo_futcode, use_container_width =True)
st.sidebar.markdown("Desenvolvido por Daniel Pessoa Soeiro")