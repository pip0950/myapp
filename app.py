import streamlit as st
import pandas as pd

st.title("Importazione file")

file_caricato = st.file_uploader(
    "Seleziona un file STEP",
    type=["stp"]
)

if file_caricato is not None:
    dati = pd.read_csv(file_caricato)

    st.success(f"File caricato: {file_caricato.name}")
    st.write("Numero di righe:", len(dati))
    st.dataframe(dati)
