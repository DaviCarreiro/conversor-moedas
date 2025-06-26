import streamlit as st
import requests

st.set_page_config(page_title="Conversor genial", layout="centered")

def buscar_taxas(moeda_origem, moeda_destino):
    url = f"https://api.exchangerate-api.com/v4/latest/{moeda_origem}"
    resultado = requests.get(url)
    dados = resultado.json()
    taxa = dados['rates'][moeda_destino]
    return taxa

moedas = ['USD', 'EUR', 'BRL', 'GBP']

moeda_origem = st.selectbox("De qual moeda:", moedas)
moeda_destino = st.selectbox("Para qual moeda:", moedas)

valor = st.number_input("Digite o valor:", min_value=0.01, value=1.0)

if st.button("Converter"):
    taxa = buscar_taxas(moeda_origem, moeda_destino)
    valor_convertido = valor * taxa
    st.success(f"{valor} {moeda_origem} = {valor_convertido:.2f} {moeda_destino}")
    st.info(f"Taxa de câmbio: 1 {moeda_origem} = {taxa:.4f} {moeda_destino}")
