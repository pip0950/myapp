import streamlit as st

st.title("Lettura file STEP")

file_step = st.file_uploader(
    "Seleziona un file STEP",
    type=["stp", "step"]
)

if file_step is not None:
    try:
        # Legge il file e lo converte in testo
        contenuto = file_step.getvalue().decode("utf-8")

        # Divide il contenuto in righe
        righe = contenuto.splitlines()

        st.success(f"File caricato: {file_step.name}")
        st.write(f"Numero di righe: {len(righe)}")

        # Mostra le righe numerate
        st.subheader("Contenuto del file")

        for numero, riga in enumerate(righe, start=1):
            st.text(f"{numero}: {riga}")

    except UnicodeDecodeError:
        st.error("Il file non è codificato in UTF-8.")
