import streamlit as st
import numpy as np
from streamlit_lottie import st_lottie
from calculospulp import load_lottieurl, solve_simplex

def calculadora():
    st.title("Calculadora Simplex Tableau")
    lottie_coding = load_lottieurl("https://lottie.host/6bca6736-6560-47b2-9647-621ae0fa2130/WRbTwyhLUj.json")
    lottie_2 = load_lottieurl("https://lottie.host/ba9e35fb-9ca4-4dd1-a9a7-24df312e9be9/vJuPUb1oux.json")

    aux = True
    aux2 = True

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Objetivo da Calculadora:")
            st.write("##")
            st.subheader("Calculadora para resolver um PPL com 2,3 ou 4 variáveis, usando método Simplex Tableau.")
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")

    with st.container():
        st.write("---")
        st.subheader("Digite quantas váriaveis de decisão e restrições o problema possui:")
        left_column, right_column = st.columns(2)
        with left_column:
            numero_dec = int(st.number_input("Váriaveis de decisão:"))
        with right_column:
            numero_res = int(st.number_input("Restrições:"))

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            c = []
            for i in range(numero_dec):
                if aux2:
                    st.header("Coeficientes da Função Objetivo")
                    aux2 = False
                coef = st.number_input(f"Coeficiente da varável x{i+1}:", value=1.0)
                c.append(coef)
            c = np.array(c)
        with right_column:
            st_lottie(lottie_2, height=300, key="2")

    A = []
    b = []

    for i in range(numero_res):
        if aux:
            st.header("Coeficientes das Restrições")
            aux = False
        st.subheader(f"Restrição {i+1}")
        constraint = []
        for j in range(numero_dec):
            coef = st.number_input(f"Coeficiente da variável x{j+1} na restrição {i+1}:", value=1.0)
            constraint.append(coef)
        lado_direito = st.number_input(f"Lado direito da restrição {i+1} (<=):", value=1.0)
        A.append(constraint)
        b.append(lado_direito)
    A = np.array(A)
    b = np.array(b)

    if st.button("Calcular solução"):
        result = solve_simplex(c, A, b, numero_dec, numero_res)
        if result['status'] == "Optimal":
            st.write("Solução Ótima Encontrada!")
            st.write(f"Valor ótimo da função objetivo (Z): {result['objective']}")
            st.write("Valores das variáveis de decisão:")
            for var, val in result['variables'].items():
                st.write(f"{var}: {val}")
        else:
            st.write("O problema não tem solução ótima.")

    st.write("[Aprenda](https://chatgpt.com)")