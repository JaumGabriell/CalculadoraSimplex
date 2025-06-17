import requests
import numpy as np
from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, value

def load_lottieurl(url):
    import requests
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def solve_simplex(c, A, b, numero_dec, numero_res):
    problem = LpProblem("Maximizar_Z", LpMaximize)
    variables = [LpVariable(chr(65 + i), lowBound=0) for i in range(numero_dec)]

    # Adicionar a função objetivo
    problem += sum(c[i] * variables[i] for i in range(numero_dec)), "Função Objetivo"

    # Adicionar restrições
    for i in range(numero_res):
        problem += sum(A[i][j] * variables[j] for j in range(numero_dec)) <= b[i], f"Restrição {i+1}"

    # Resolver o problema
    problem.solve()

    status = LpStatus[problem.status]
    # Checar se todas variáveis têm valor e se o valor da função objetivo é significativamente positivo
    variaveis_validas = all(v.varValue is not None for v in variables)
    valor_objetivo_valido = value(problem.objective) is not None and value(problem.objective) > 1e-6

    if status == 'Optimal' and variaveis_validas and valor_objetivo_valido:
        shadow_prices = {f"Restrição {i+1}": c.pi for i, c in enumerate(problem.constraints.values())}
        result = {
            'status': status,
            'objective': value(problem.objective),
            'variables': {chr(65 + i): variables[i].varValue for i in range(numero_dec)},
            'shadow_prices': shadow_prices,
        }
    else:
        result = {
            'status': status,
            'objective': None,
            'variables': None,
            'shadow_prices': None,
        }

    return result
