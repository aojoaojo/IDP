from flask import Flask, render_template, request
from simplex import *

app = Flask(__name__)

# Processa as restrições e a função objetivo
def processar_input(funcao_objetivo, restricoes):
    """
    Processa a entrada de função objetivo e restrições fornecida pelo usuário.

    Args:
        funcao_objetivo: String com os coeficientes da função objetivo.
        restricoes: String com as restrições no formato "a,b,c\nx,y,z".

    Retorna:
        A, b, funcao_objetivo: Matriz A das restrições, vetor b, e vetor da função objetivo.
    """
    # Processa função objetivo
    funcao_objetivo = [float(x) for x in funcao_objetivo.split(',')]

    # Processa restrições - múltiplas linhas
    restricoes = [[float(num) for num in linha.split(',')] for linha in restricoes.splitlines()]
    
    A = [linha[:-1] for linha in restricoes]
    b = [linha[-1] for linha in restricoes]
    
    return A, b, funcao_objetivo

@app.route('/', methods=['GET', 'POST'])
def branch_and_bound_solver():
    """
    Rota principal do aplicativo. Processa a entrada do usuário e resolve o problema usando Branch and Bound.

    Retorna:
        Página renderizada com os resultados do Branch and Bound.
    """
    melhor_solucao, melhor_valor = None, None
    tabela = None
    if request.method == 'POST':
        funcao_objetivo = request.form.get('funcao_objetivo')
        restricoes = request.form.get('restricoes')
        
        # Chamando a função do Branch and Bound
        melhor_solucao, melhor_valor = branch_and_bound(funcao_objetivo, restricoes)
    
    return render_template('index_branch_and_bound.html', 
                           melhor_solucao=melhor_solucao, 
                           melhor_valor=melhor_valor, 
                           tabela=tabela)

if __name__ == '__main__':
    app.run(debug=True)
