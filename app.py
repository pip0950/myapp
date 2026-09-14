import streamlit as st
from pathlib import Path

st.title("La mia applicazione")

nome = st.text_input("Come ti chiami?")

if nome:
    st.write(f"Ciao, {nome}!")
