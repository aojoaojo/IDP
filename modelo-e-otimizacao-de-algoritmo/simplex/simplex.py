def copiar_matriz(matriz):
    """Retorna uma cópia da matriz.
    
    Args:
        matriz: A matriz a ser copiada.

    Retorna:
        A cópia da matriz.            
    """
    return [linha[:] for linha in matriz]

def escalonar_matriz(matriz):
    """Escalona a matriz e retorna a matriz escalonada. Também retorna o número de trocas de linha.
    
    Args:
        matriz: A matriz a ser escalonada.

    Retorna:
        A matriz escalonada e o número de trocas de linha.
    """
    matriz = copiar_matriz(matriz)
    if matriz is None:
        return None, 0

    n = len(matriz)
    m = len(matriz[0])
    trocas_linhas = 0

    for i in range(min(n, m)):
        if matriz[i][i] == 0:
            for j in range(i + 1, n):
                if matriz[j][i] != 0:
                    matriz[i], matriz[j] = matriz[j], matriz[i]
                    trocas_linhas += 1
                    break

        pivot = matriz[i][i]
        if pivot != 0:
            for j in range(i + 1, n):
                fator = matriz[j][i] / matriz[i][i]
                for k in range(i, m):
                    matriz[j][k] -= fator * matriz[i][k]

    return matriz, trocas_linhas

def calcular_determinante(matriz):
    """Calcula a determinante de uma matriz quadrada a partir de sua matriz escalonada.
    
    Args:
        matriz: A matriz a ser calculada.

    Retorna:
        O valor do determinante.
    """
    matriz_escalonada, trocas_linhas = escalonar_matriz(matriz)
    n = len(matriz)
    
    determinante = 1
    for i in range(n):
        determinante *= matriz_escalonada[i][i]

    if trocas_linhas % 2 != 0:
        determinante *= -1
    
    return determinante

def inversa_matriz(matriz):
    """Calcula a inversa de uma matriz usando o método de escalonamento.
    
    Args:
        matriz: A matriz a ser invertida.

    Retorna:
        A matriz inversa, ou None se a matriz não for quadrada.
    """
    n = len(matriz)
    if n != len(matriz[0]):
        return None
    
    identidade = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    matriz_extendida = [matriz[i] + identidade[i] for i in range(n)]
    
    for i in range(n):
        pivot = matriz_extendida[i][i]
        if pivot == 0:
            for j in range(i + 1, n):
                if matriz_extendida[j][i] != 0:
                    matriz_extendida[i], matriz_extendida[j] = matriz_extendida[j], matriz_extendida[i]
                    break
            pivot = matriz_extendida[i][i]

        for j in range(i, 2 * n):
            matriz_extendida[i][j] /= pivot

        for j in range(n):
            if j != i:
                fator = matriz_extendida[j][i]
                for k in range(i, 2 * n):
                    matriz_extendida[j][k] -= fator * matriz_extendida[i][k]

    inversa = [linha[n:] for linha in matriz_extendida]
    return inversa

def multiplicar_matrizes(matriz1, matriz2):
    """Multiplica duas matrizes.
    
    Args:
        matriz1: A primeira matriz.
        matriz2: A segunda matriz.

    Retorna:
        A matriz resultante da multiplicação.
    """
    if len(matriz1[0]) != len(matriz2):
        return None
    
    resultado = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz1))]
    
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    
    return resultado

def inicializar_tabela_simplex(A, b, c):
    """
    Inicializa a tabela Simplex para o problema.

    Parâmetros:
    - A: matriz de coeficientes das restrições (lista de listas).
    - b: vetor de termos independentes (lista).
    - c: vetor de coeficientes da função objetivo (lista).

    Retorna:
    - tabela_simplex: a tabela Simplex inicializada (lista de listas).
    """
    num_restricoes = len(A)
    num_variaveis = len(A[0])

    tabela_simplex = []

    for i in range(num_restricoes):
        linha = A[i] + [0] * num_restricoes + [b[i]]
        linha[num_variaveis + i] = 1
        tabela_simplex.append(linha)

    linha_objetivo = c + [0] * (num_restricoes + 1)
    tabela_simplex.append(linha_objetivo)

    return tabela_simplex

def encontrar_pivot(tabela_simplex):
    """
    Encontra o elemento pivot na tabela Simplex.

    Args:
        tabela_simplex: Matriz representando a tabela Simplex (inclui a função objetivo e as restrições).

    Retorna:
        A linha e a coluna do elemento
    """
    coluna_pivot = min((valor, idx) for idx, valor in enumerate(tabela_simplex[-1][:-1]))[1]
    if all(linha[coluna_pivot] <= 0 for linha in tabela_simplex[:-1]):
        return None, None

    linha_pivot = min((tabela_simplex[i][-1] / tabela_simplex[i][coluna_pivot], i)
                      for i in range(len(tabela_simplex) - 1)
                      if tabela_simplex[i][coluna_pivot] > 0)[1]

    return linha_pivot, coluna_pivot

def realizar_operacoes_simplex(tabela_simplex, linha_pivot, coluna_pivot):
    """
    Realiza as operações da iteração do método Simplex.

    Args:
        tabela_simplex: Matriz representando a tabela Simplex (inclui a função objetivo e as restrições).
        linha_pivot: Índice da linha pivot.
        coluna_pivot: Índice da coluna pivot.

    Retorna:
        A nova tabela Simplex após a iteração.
    """

    elemento_pivot = tabela_simplex[linha_pivot][coluna_pivot]
    tabela_simplex[linha_pivot] = [x / elemento_pivot for x in tabela_simplex[linha_pivot]]

    for i in range(len(tabela_simplex)):
        if i != linha_pivot:
            fator = tabela_simplex[i][coluna_pivot]
            tabela_simplex[i] = [x - fator * y for x, y in zip(tabela_simplex[i], tabela_simplex[linha_pivot])]

    return tabela_simplex

def verificar_solucao_otima(tabela_simplex):
    """
    Função que verifica se a solução atual é ótima.
    
    Args:
        tabela_simplex: Matriz representando a tabela Simplex (inclui a função objetivo e as restrições).
        
    Retorna:
        True se a solução for ótima (todos os coeficientes da função objetivo >= 0), False caso contrário.
    """
    funcao_objetivo = tabela_simplex[-1]

    for coeficiente in funcao_objetivo[:-1]:
        if coeficiente < 0:
            return False
    
    return True

def tratar_matriz_simplex_final(tabela_simplex):
    """
    Função que trata a matriz final da tabela Simplex, facilitando a saída do programa.
    
    Args:
        tabela_simplex: Matriz representando a tabela Simplex (inclui a função objetivo e as restrições).
        
    Retorna:
        As variáveis básicas e seus respectivos valores.
        As variáveis não básicas e seus valores
    """

    num_variaveis_basicas = len(tabela_simplex) - 1

    num_variaveis_nao_basicas = len(tabela_simplex[0]) - num_variaveis_basicas - 1

    variaveis_basicas = {}
    variaveis_nao_basicas = {}

    for i in range(num_variaveis_basicas):

        coluna_variavel = [linha[i] for linha in tabela_simplex[:-1]]
        
        if coluna_variavel.count(0) == len(coluna_variavel) - 1 and coluna_variavel.count(1) == 1:
            variavel = coluna_variavel.index(1)
            valor = tabela_simplex[variavel][-1]
            variaveis_basicas[f'x_{i + 1}'] = round(valor, 4)

    for i in range(num_variaveis_nao_basicas):
        variaveis_nao_basicas[f'x_{num_variaveis_basicas + i + 1}'] = 0
    
    return variaveis_basicas, variaveis_nao_basicas
    
def todo_o_processo(funcao_objetivo, restricoes):
    c = list(funcao_objetivo.split(','))
    for i in range(len(c)):
        c[i] = float(c[i])
    A_b = [list(map(float, linha.split(','))) for linha in restricoes.split('\r')]
    A = [linha[:-1] for linha in A_b]
    b = [linha[-1] for linha in A_b]

    tabela_simplex = inicializar_tabela_simplex(A, b, c)

    iteracoes = 0
    while not verificar_solucao_otima(tabela_simplex):
        iteracoes += 1
        linha_pivot, coluna_pivot = encontrar_pivot(tabela_simplex)
        if linha_pivot is None:
            return f"Problema não tem solução viável ou ilimitada. Iterações: {iteracoes}"
        tabela_simplex = realizar_operacoes_simplex(tabela_simplex, linha_pivot, coluna_pivot)

    variaveis_basicas, variaveis_nao_basicas = tratar_matriz_simplex_final(tabela_simplex)

    return f"Solução encontrada após {iteracoes} iterações.", tabela_simplex, variaveis_basicas, variaveis_nao_basicas