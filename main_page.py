import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime 
from helper import Helper




if "data" not in st.session_state:

    st.session_state["data"] = Helper.load_main_file


st.markdown("# SISTEMA FUTCODE DE MONITORAMENTO E RECOMENDAÇÃO DE ATLETAS! ⚽️")
st.sidebar.markdown("Desenvolvido por Daniel Pessoa Soeiro")