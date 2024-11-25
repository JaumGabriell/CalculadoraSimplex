import requests
import numpy as np
from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, value

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def solve_simplex(c, A, b, numero_dec, numero_res):
    problem = LpProblem("Maximizar_Z", LpMaximize)
    variables = [LpVariable(chr(65 + i), lowBound=0) for i in range(numero_dec)]

    problem += sum(c[i] * variables[i] for i in range(numero_dec)), "Função Objetivo"

    for i in range(numero_res):
        problem += sum(A[i][j] * variables[j] for j in range(numero_dec)) <= b[i], f"Restrição {i+1}"

    problem.solve()

    result = {
        'status': LpStatus[problem.status],
        'objective': value(problem.objective),
        'variables': {chr(65 + i): variables[i].varValue for i in range(numero_dec)}
    }

    return result