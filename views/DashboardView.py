class DashboardView:
    def __init__(self, streamlit) -> None:
        self.streamlit = streamlit

    def content(self, streamlit_container):
        with streamlit_container:
            with self.streamlit.spinner("Aguarde ..."):  
                streamlit_container.header("Dashboard")