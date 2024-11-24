import streamlit as st
import requests
from streamlit_lottie import st_lottie
import numpy as np
from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, value

# função para colocar gifs

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

# Funções para cada página
def home():
    st.markdown("<h1 style='text-align: center;'>Bem-vindos ao projeto de otimização</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Calculadora para resolver um PPL com 2,3 ou 4 variáveis, usando método Simplex Tableau.</h2>", unsafe_allow_html=True)
    st.markdown("<div style='position: fixed; bottom: 0; left: 0.1%; width: 80%; text-align: center;'>Alunos: Juju, Gugu e Dudu</div>", unsafe_allow_html=True)
    lottie_3= load_lottieurl("https://lottie.host/a18fb9d0-abb3-4742-86d2-7b05571aa0ff/aFkb35Gdbl.json")
    st_lottie(lottie_3, height=300,key="3")


def contato():
    st.title("Nos contate")
    st.write("Qualquer duvida só nos chamar.")
    # bobeira q eu quis fazer só pra ver se funciona, só serve pra mandar email pra mim msm
    with st.container():
        st.write("---")
        st.header("Contato:")
        st.write("##")

        st.markdown(
            """
            <style>
            input[type="text"], input[type="email"], textarea {
            width: 100%;
            padding: 12px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
            margin-top: 6px;
            margin-bottom: 16px;
            resize: vertical;
            }
            button[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 14px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            }
            button[type="submit"]:hover {
            background-color: #45a049;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        contact_form = """
        <form action="https://formsubmit.co/contasecundariaminha123@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder = "Seu nome" required>
        <input type="email" name="email" placeholder="Seu email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()

def calculadora():
    st.title("Calculadora Simplex Tableau")
    


    lottie_coding = load_lottieurl("https://lottie.host/6bca6736-6560-47b2-9647-621ae0fa2130/WRbTwyhLUj.json")
    lottie_2= load_lottieurl("https://lottie.host/ba9e35fb-9ca4-4dd1-a9a7-24df312e9be9/vJuPUb1oux.json")

    # var auxiliares
    aux = True
    aux2 = True

    #=============================================================================================================================================================================#

    # explicação do objetivo da calculadora


    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Objetivo da Calculadora:")
            st.write("##") # da um espaço pro próximo elemento
            st.subheader(
                """
                Calculadora para resolver um PPL com 2,3 ou 4 variáveis, usando método Simplex Tableau.

                """
            )
        with right_column: 
            st_lottie(lottie_coding, height=300,key="coding")

    #=============================================================================================================================================================================#


    # escrevendo as variaveis principais do problema

    with st.container():
        st.write("---")
        #st.markdown("<h1 style='text-align: center;'>Digite as váriaveis de decisão e quantas restrições o problema possui</h1>", unsafe_allow_html=True)
        st.subheader("Digite quantas váriaveis de decisão e restrições o problema possui:")
        left_column, right_column = st.columns(2)
        with left_column:
            numero_dec = int(st.number_input("Váriaveis de decisão:"))
        with right_column: 
            numero_res = int(st.number_input("Restrições:"))

    #=============================================================================================================================================================================#

    # escrevendo os coeficientes da função objetivo

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            # o "for" aqui vai gerar linhas para escrever de acordo com quantos coeficientes coloquei q a questão vai ter
            c= []
            for i in range(numero_dec):
                if(aux2):
                    st.header("Coeficientes da Função Objetivo")
                    aux2 = False
                coef = st.number_input(f"Coeficiente da varável x{i+1}:", value= 1.0)
                c.append(coef)
            c = np.array(c)
        with right_column: 
            st_lottie(lottie_2, height=300,key="2")

    #=============================================================================================================================================================================#

    # Entrada das restrições

    A = []
    b = []

    # o for basicamente vai gerar o número de restrições com base no coeficiente e no quanto de restrições falamos q o problema vai ter váriaveis

    for i in range(numero_res):
        if (aux):
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

    #=============================================================================================================================================================================#

    # Criando o modelo de programação linear com o PuLP
    if st.button("Calcular solução"):
        # Criando o problema de maximização
        problem = LpProblem("Maximizar_Z", LpMaximize)

        # Definindo as variáveis de decisão como A, B, C, etc.
        variables = [LpVariable(chr(65 + i), lowBound=0) for i in range(numero_dec)]  # Variáveis 'A', 'B', 'C', etc.

        # Adicionando a função objetivo
        problem += sum(c[i] * variables[i] for i in range(numero_dec)), "Função Objetivo"

        # Adicionando as restrições
        for i in range(numero_res):
            problem += sum(A[i][j] * variables[j] for j in range(numero_dec)) <= b[i], f"Restrição {i+1}"

        # Resolvendo o problema
        problem.solve()

        # Exibindo os resultados
        if LpStatus[problem.status] == "Optimal":
            st.write("Solução Ótima Encontrada!")
            st.write(f"Valor ótimo da função objetivo (Z): {value(problem.objective)}")
            st.write("Valores das variáveis de decisão:")
            for i in range(numero_dec):
                st.write(f"{chr(65 + i)}: {variables[i].varValue}")  # Exibindo 'A', 'B', 'C', etc.
        else:
            st.write("O problema não tem solução ótima.")


    st.write("[Aprenda](https://chatgpt.com)")



# Dicionário de páginas
pages = {
    "Inicío": home,
    "Contato": contato,
    "Calculadora": calculadora,
}

# Seleção de página
page = st.sidebar.selectbox("Select a page", list(pages.keys()))

# Executa a função da página selecionada
pages[page]()