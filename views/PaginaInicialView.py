class PaginaInicialView:
    def __init__(self, streamlit) -> None:
        self.streamlit = streamlit

    def content(self, streamlit_container):
        with streamlit_container:
            with self.streamlit.spinner("Aguarde ..."):    
                streamlit_container.header("Streamlit - DataBoard")
                streamlit_container.subheader("Projeto de apresentação de dashboards com templates prontos")
                streamlit_container.write("Autor: Jonathan Greco")