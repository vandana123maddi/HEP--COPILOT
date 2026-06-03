
import streamlit as st
st.title("HEP Copilot")
query = st.text_input("Ask a HEP question")
if query:
    st.write("Query:", query)
