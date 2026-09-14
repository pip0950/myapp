import streamlit as st

st.set_page_config(page_title="Lettore STEP")

st.title("Lettore di file STEP")
st.write("Carica un file con estensione .stp oppure .step")

file_step = st.file_uploader(
    "Scegli il file STEP",
    type=["stp", "step"]
)

if file_step is not None:
    dati_file = file_step.getvalue()

    try:
        contenuto = dati_file.decode("utf-8")
    except UnicodeDecodeError:
        try:
            contenuto = dati_file.decode("latin-1")
        except Exception:
            st.error("Impossibile leggere il file.")
            st.stop()

    righe = contenuto.splitlines()

    st.success(f"File caricato: {file_step.name}")
    st.write(f"Righe lette: {len(righe)}")

    # Pulsante per visualizzare o nascondere tutte le righe
    if st.checkbox("Visualizza tutte le righe"):
        for numero, riga in enumerate(righe, start=1):
            st.text(f"{numero}: {riga}")

    # Esempio: mostra solo le righe che contengono ENTITY
    righe_entity = [
        riga for riga in righe
        if "ENTITY" in riga.upper()
    ]

    st.subheader("Righe contenenti ENTITY")
    st.write(f"Trovate: {len(righe_entity)}")

    for riga in righe_entity:
        st.code(riga)
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
