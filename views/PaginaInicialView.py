import pandas as pd

class PaginaInicialView:
    def __init__(self, streamlit) -> None:
        self.streamlit = streamlit

    def content(self, streamlit_container):
        with streamlit_container:
            with self.streamlit.spinner("Aguarde ..."):    
                streamlit_container.header("Streamlit - DataBoard")
                streamlit_container.subheader("Projeto de apresentação de dashboards com templates prontos")
                streamlit_container.write("Autor: Jonathan Greco")

    def combo_templates_sidebar_changeevent(self, streamlit_container):

        #for key, value in kwargs.items():
        #    print("%s == %s" % (key, value))
        combo_value = self.streamlit.session_state.combo_templates_sidebar
        
        print(f"Upload {combo_value}")
        with streamlit_container:
            with self.streamlit.spinner("Aguarde ..."):
                uploaded_file = streamlit_container.file_uploader("Escolha um arquivo CSV", 
                                                                  key='upload_templates_sidebar', 
                                                                  type=['CSV', 'XLSX'], 
                                                                  on_change=self.upload_templates_sidebar_changeevent,
                                                                  args=[streamlit_container],  
                                                                  )
                
    def upload_templates_sidebar_changeevent(self, container=None):
        file = self.streamlit.session_state.upload_templates_sidebar
        if file is not None:            
            #with st("Carregando dados do arquivo ..."):
            data = pd.read_csv(file, delimiter=',')

            self.streamlit.session_state.menu_templates_sidebar = True
            self.streamlit.session_state.data_upload_templates_sidebar['filename'] = file.name
            self.streamlit.session_state.data_upload_templates_sidebar['data'] = data
          