import streamlit as st

st.title("Il mio programma")

nome = st.text_input("Inserisci il nome")
numero = st.number_input(
    "Inserisci un numero",
    min_value=0,
    step=1
)

if st.button("Esegui"):
    risultato = numero * 2
    st.success(f"{nome}, il risultato è {risultato}")
