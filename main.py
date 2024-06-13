import streamlit as st
import pandas as pd
import numpy as np
import time
from io import StringIO

from views.PaginaInicialView import PaginaInicialView
from views.DashboardView import DashboardView
from views.TabelaView import TabelaView

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

sidebar_logo = 'images/logotipo-sidebar-1.png'
st.logo(sidebar_logo)

#layout do container central
container = st.container(border=False)

#layout do sidebar
with st.sidebar:

    #botao inicial do menu sidebar
    button_inicial_sidebar = st.button("Início", type="secondary", use_container_width=True)
    if button_inicial_sidebar:
        pagina_inicial_view = PaginaInicialView(st)
        pagina_inicial_view.content(container)

    add_selectbox = st.sidebar.selectbox(
        "Templates",
        index=None,        
        placeholder="Selecione um template",
        options=("Investimentos B3", "Controle de estoque", "Finanças pessoais", "Gastos cartão de crédito")
    )
    
    #botoes do menu sidebar
    button_dashboard_sidebar = st.button("Dashboard", type="secondary", use_container_width=True)
    if button_dashboard_sidebar:
        print("Dashboard")          
        dashboard_view = DashboardView(st)    
        dashboard_view.content(container)       

    button_tabela_sidebar = st.button("Tabela de dados", type="secondary", use_container_width=True)
    if button_tabela_sidebar:
        tabela_view = TabelaView(st)
        tabela_view.content(container) 

    button_formulario_sidebar = st.button("Formulário", type="secondary", use_container_width=True)
    if button_formulario_sidebar:
        pass
    
