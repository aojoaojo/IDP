from flask import Flask, render_template, request
from simplex import *

app = Flask(__name__)

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
