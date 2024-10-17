from flask import Flask, render_template, request
import simplex

app = Flask(__name__)

# Processa as restrições e a função objetivo
def processar_input(funcao_objetivo, restricoes):
    # Processa função objetivo
    funcao_objetivo = [float(x) for x in funcao_objetivo.split(',')]

    # Processa restrições - múltiplas linhas
    restricoes = [[float(num) for num in linha.split(',')] for linha in restricoes.splitlines()]
    
    A = [linha[:-1] for linha in restricoes]
    b = [linha[-1] for linha in restricoes]
    
    return A, b, funcao_objetivo

@app.route('/', methods=['GET', 'POST'])
def simplex_solver():
    resultado, tabela, variaveis_basicas, variaveis_nao_basicas = None, None, None, None
    if request.method == 'POST':
        funcao_objetivo = request.form.get('funcao_objetivo')
        restricoes = request.form.get('restricoes')
        
        resultado, tabela, variaveis_basicas, variaveis_nao_basicas = simplex.todo_o_processo( funcao_objetivo, restricoes )
        
    return render_template('index.html',  resultado=resultado, tabela=tabela, variaveis_basicas=variaveis_basicas, variaveis_nao_basicas=variaveis_nao_basicas)

if __name__ == '__main__':
    app.run(debug=True)
