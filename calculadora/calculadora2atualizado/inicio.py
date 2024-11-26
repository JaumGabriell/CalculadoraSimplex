import streamlit as st
from streamlit_lottie import st_lottie
from calculospulp import load_lottieurl

def home():
    st.markdown("<h1 style='text-align: center;'>Bem-vindos ao projeto de otimização</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Calculadora para resolver um PPL com 2,3 ou 4 variáveis, usando método Simplex Tableau.</h2>", unsafe_allow_html=True)
    st.markdown("<div style='position: fixed; bottom: 0; left: 0.1%; width: 80%; text-align: center;'>Alunos: Juju, Gugu e Dudu</div>", unsafe_allow_html=True)
    lottie_3 = load_lottieurl("https://lottie.host/a18fb9d0-abb3-4742-86d2-7b05571aa0ff/aFkb35Gdbl.json")
    st_lottie(lottie_3, height=300, key="3")