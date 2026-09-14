import streamlit as st, nom, numer
from pathlib import Path

st.title("La mia applicazione")

nome = st.text_input("Come ti chiami?")

if nome:
    st.write(f"Ciao, {nome}!")

nome = nom.text_input("Inserisci il nome: ")
numero = int(numer.text_input("Inserisci un numero: "))

risultato = numero * 2

 numero.write(f"{nom}, il risultato è {risultato}")
