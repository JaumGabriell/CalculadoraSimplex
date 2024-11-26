import streamlit as st
import numpy as np
from streamlit_lottie import st_lottie
from calculospulp import load_lottieurl, solve_simplex

def calculadora():
    st.title("Calculadora Simplex Tableau")
    lottie_coding = load_lottieurl("https://lottie.host/6bca6736-6560-47b2-9647-621ae0fa2130/WRbTwyhLUj.json")

    # Inicializar Session State
    if 'c' not in st.session_state:
        st.session_state.c = []
    if 'A' not in st.session_state:
        st.session_state.A = []
    if 'b' not in st.session_state:
        st.session_state.b = []
    if 'result' not in st.session_state:
        st.session_state.result = None

    # Entrada inicial
    st.subheader("Digite o número de variáveis de decisão e restrições:")
    numero_dec = int(st.number_input("Variáveis de decisão:", min_value=2, max_value=4, value=2))
    numero_res = int(st.number_input("Restrições:", min_value=1, value=2))

    # Coletar função objetivo
    st.header("Coeficientes da Função Objetivo")
    c = []
    for i in range(numero_dec):
        coef = st.number_input(f"Coeficiente de x{i+1}:", value=1.0, key=f"c_{i}")
        c.append(coef)
    st.session_state.c = np.array(c)

    # Coletar restrições
    st.header("Coeficientes das Restrições")
    A = []
    b = []
    for i in range(numero_res):
        st.subheader(f"Restrição {i+1}")
        constraint = []
        for j in range(numero_dec):
            coef = st.number_input(f"Coeficiente de x{j+1} na restrição {i+1}:", value=1.0, key=f"A_{i}_{j}")
            constraint.append(coef)
        lado_direito = st.number_input(f"Lado direito da restrição {i+1} (<=):", value=1.0, key=f"b_{i}")
        A.append(constraint)
        b.append(lado_direito)
    st.session_state.A = np.array(A)
    st.session_state.b = np.array(b)

    # Solução inicial
    if st.button("Calcular solução"):
        st.session_state.result = solve_simplex(st.session_state.c, st.session_state.A, st.session_state.b, numero_dec, numero_res)

    # Mostrar resultados
    if st.session_state.result:
        result = st.session_state.result
        if result['status'] == "Optimal":
            st.success("Solução Ótima Encontrada!")
            st.write(f"Valor ótimo da função objetivo (Z): {result['objective']}")
            st.write("Valores das variáveis de decisão:")
            for var, val in result['variables'].items():
                st.write(f"{var}: {val}")
            st.write("Preços sombra das restrições:")
            for restricao, preco in result['shadow_prices'].items():
                st.write(f"{restricao}: {preco}")

            # Ajuste de valores
            st.subheader("Ajuste no lado direito das restrições:")
            novos_b = []
            for i in range(numero_res):
                novo_valor = st.number_input(f"Novo valor para a restrição {i+1}:", value=float(st.session_state.b[i]), key=f"novo_b_{i}")
                novos_b.append(novo_valor)
            novos_b = np.array(novos_b)

            # Recalcular
            if st.button("Recalcular com novos valores"):
                novo_result = solve_simplex(st.session_state.c, st.session_state.A, novos_b, numero_dec, numero_res)
                if novo_result['status'] == "Optimal":
                    st.success("Nova solução ótima encontrada!")
                    st.write(f"Novo valor ótimo da função objetivo (Z): {novo_result['objective']}")
                else:
                    st.error("A alteração não é válida. O problema não tem solução ótima.")
        else:
            st.error("O problema não tem solução ótima.")
