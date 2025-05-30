import requests
import streamlit as st 

def buscar_letra(banda, musica):
    url = f'https://api.lyrics.ovh/v1/{banda}/{musica}'
    response = requests.get(url)
    letra = response.json()["lyrics"] if response.status_code == 200 else ""
    return letra

st.title("Letras de musicas")

banda = st.text_input("Digite o nome da banda: ", key="banda")
musica = st.text_input("Digite o nome da musica: ", key="musica")
pesquisar = st.button("Pesquisar")

if pesquisar:
    letra = buscar_letra(banda, musica)
    if letra:
        st.success("Encontramos a letra da musica")
        st.text(letra)
    else:
        st.error("Não foi possivel localizar a musica")
