import streamlit as st

st.title("Lettura file STEP")

file_step = st.file_uploader(
    "Seleziona un file STEP",
    type=["stp", "step"]
)

if file_step is not None:
    contenuto = file_step.getvalue().decode("latin-1")

    # Mantiene i caratteri di fine riga
    prime_10_righe = contenuto.splitlines(keepends=True)[:10]
    testo_da_salvare = "".join(prime_10_righe)

    st.subheader("Prime 10 righe")
    st.code(testo_da_salvare, language="text")

    st.download_button(
        "Scarica il file TXT",
        data=testo_da_salvare.encode("utf-8"),
        file_name="prime_10_righe.txt",
        mime="text/plain"
    )
