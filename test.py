import streamlit as st
import requests
from streamlit_lottie import st_lottie
import numpy as np
from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, value



# título da pagina

st.set_page_config(page_title="Calculadora PPL", page_icon=":alien:", layout="wide")

#=============================================================================================================================================================================#

# função para colocar gifs

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/6bca6736-6560-47b2-9647-621ae0fa2130/WRbTwyhLUj.json")
lottie_2= load_lottieurl("https://lottie.host/307b72ed-710a-4b01-8024-ad982b9c77df/5tqltb6XzO.json")

#=============================================================================================================================================================================#

# aqui era só pra tentar deixar os contatos mais bonitinho mas ta dando erro

#use local CSS
#
#def local_css(file_name):
 #   with open(file_name) as f:
  #      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#local_css("style/style")#

#=============================================================================================================================================================================#

# var auxiliares
aux = True
aux2 = True

#=============================================================================================================================================================================#

# cabeçalho 

st.markdown("<h1 style='text-align: center;'>Projeto de otimização</h1>", unsafe_allow_html=True)
st.subheader("Alunos: || :ghost:")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Objetivo")
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
    st.subheader("Digite quantas váriaveis de decisão e restrições o problema possui")
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

#=============================================================================================================================================================================#


# bobeira q eu quis fazer só pra ver se funciona, só serve pra mandar email pra mim msm
with st.container():
    st.write("---")
    st.header("Contato:")
    st.write("##")

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
