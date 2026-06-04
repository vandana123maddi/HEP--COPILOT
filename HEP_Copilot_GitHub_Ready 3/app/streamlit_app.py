import streamlit as st
import plotly.express as px
from analysis.router import route_query

st.title("HEP Copilot")

query = st.text_input(
    "Ask a High Energy Physics question"
)

if st.button("Run"):

    result = route_query(query)

    st.write(result)

    if isinstance(result, dict) and "sample_masses" in result:

        fig = px.histogram(
            x=result["sample_masses"],
            nbins=20,
            title="Dimuon Mass Distribution"
        )

        st.plotly_chart(fig)
