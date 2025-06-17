import streamlit as st
from inicio import home
from contato import contato
from calculadora import calculadora

# Dicionário de páginas
pages = {
    "Inicío": home,
    "Calculadora": calculadora,
    "Contato": contato,
}

# Seleção de página
page = st.sidebar.selectbox("Select a page", list(pages.keys()))

# Executa a função da página selecionada
pages[page]()