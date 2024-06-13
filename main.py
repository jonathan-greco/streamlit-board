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

#states
if 'combo_templates_sidebar' not in st.session_state:
    st.session_state.combo_templates_sidebar = None
if 'menu_templates_sidebar' not in st.session_state:
    st.session_state.menu_templates_sidebar = False
if 'upload_templates_sidebar' not in st.session_state:
    st.session_state.upload_templates_sidebar = None    
if 'data_upload_templates_sidebar' not in st.session_state:
    st.session_state.data_upload_templates_sidebar = dict(filename='', data=None)

#Layout
sidebar_logo = 'images/logotipo-sidebar-1.png'
st.logo(sidebar_logo)

#layout do container central
container = st.container(border=False)

#layout do sidebar
with st.sidebar:   
    pagina_inicial_view = PaginaInicialView(st)
    #botao inicial do menu sidebar
    button_inicial_sidebar = st.button("Início", type="secondary", use_container_width=True)
    if button_inicial_sidebar:
        #container.empty()  
        container.empty()              
        st.session_state.combo_templates_sidebar = None
        st.session_state.menu_templates_sidebar = False
        st.session_state.upload_templates_sidebar = None
        st.session_state.data_upload_templates_sidebar = dict(filename='', data=None)
        pagina_inicial_view.content(container)

    #combo
    combo_templates_sidebar = st.selectbox(
            "Templates",
            index=None,     
            key='combo_templates_sidebar',
            placeholder="Selecione um template",
            options=("Investimentos B3", "Controle de estoque", "Finanças pessoais", "Gastos cartão de crédito"),
            on_change=pagina_inicial_view.combo_templates_sidebar_changeevent,
            args=[container],            
        )
    
    #if combo_templates_sidebar:
    #    container.dataframe(st.session_state.dataupload_templates_sidebar, use_container_width=True)
    #    st.session_state['combo_templates_sidebar'] = add_selectbox
    #    pagina_inicial_view = PaginaInicialView(st)
    #    pagina_inicial_view.combo_templates_sidebar_changeevent(container)

    #if st.session_state.upload_templates_sidebar:
       # if st.session_state.upload_templates_sidebar is not None:
            #with st.spinner("Carregando dados do arquivo ..."):
                #data = pd.read_csv(st.session_state.upload_templates_sidebar, delimiter=',')

                #container.write(st.session_state.upload_templates_sidebar.name)
                #self.streamlit.session_state.menu_templates_sidebar = True
    
    #botoes do menu sidebar
    if st.session_state.menu_templates_sidebar == True:
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
    
with container:
    container.empty()