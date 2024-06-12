import streamlit as st
import pandas as pd
import numpy as np
import time
from io import StringIO

#configs
st.set_page_config(
    page_title="DataBoard em StreamLit",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# DataBoard v.1.0 - Autor: Jonathan Greco"
    }
)

st.title('Página principal')

sidebar_logo = 'images/logotipo-sidebar-1.png'
st.logo(sidebar_logo)

st.header("Streamlit - DataBoard")
st.subheader("Projeto de apresentação de dashboards com templates prontos")
st.write("Autor: Jonathan Greco")