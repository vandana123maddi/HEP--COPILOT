
import streamlit as st
from analysis.router import route_query

st.title("HEP Copilot")

query = st.text_input(
    "Ask a High Energy Physics question"
)

if st.button("Run"):

    result = route_query(query)

    st.success(result)

