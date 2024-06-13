class TabelaView:
    def __init__(self, streamlit) -> None:
        self.streamlit = streamlit

    def content(self, streamlit_container):
        with streamlit_container:
            with self.streamlit.spinner("Aguarde ..."):  
                streamlit_container.header("Tabela de dados")  

                filename = self.streamlit.session_state.data_upload_templates_sidebar['filename']   
                data = self.streamlit.session_state.data_upload_templates_sidebar['data']

                if filename:
                    streamlit_container.write(filename)
                    streamlit_container.dataframe(data, use_container_width=True, key='dataframe_container_mod_tabela') 