def dividir_lista(lista, tamanho):
    return [lista[i:i + tamanho] for i in range(0, len(lista), tamanho)]

def trata_array_de_tamanhos_maximos_float(array_de_tamanhos_maximos_float, matriz):
    max_float_por_coluna = []
    for sublista in array_de_tamanhos_maximos_float:
        if max(sublista) > 1:
            for i in range(len(matriz[0])):
                for linha in matriz:
                    partes = str(linha[i]).split('.')
                    max_float_por_coluna.append(len(partes[1]) if len(partes) > 1 else 0)
    return dividir_lista(max_float_por_coluna, len(matriz[0]))

def maximos_por_coluna(array_de_tamanhos_maximos, max_float_por_coluna):
    maximo_por_coluna, maximo_por_coluna_float = [], []

    for i in array_de_tamanhos_maximos:
        maximo_por_coluna.append(max(i))

    for i in max_float_por_coluna:
        maximo_por_coluna_float.append(max(i))
    return maximo_por_coluna, maximo_por_coluna_float

def pegar_tamanho_maximo(matriz):
    array_de_tamanhos_maximos = []
    array_de_tamanhos_maximos_float = []

    for linha in matriz:
        for valor in linha:
            inteiro, fracionario = str(valor).split('.')[0], str(valor).split('.')[1] if '.' in str(valor) else ''
            array_de_tamanhos_maximos.append(len(inteiro))
            array_de_tamanhos_maximos_float.append(len(fracionario))

    return dividir_lista(array_de_tamanhos_maximos, len(matriz[0])), dividir_lista(array_de_tamanhos_maximos_float, len(matriz[0]))

def print_matriz(matriz, decimais=None):
    array_de_tamanhos_maximos, array_de_tamanhos_maximos_float = pegar_tamanho_maximo(matriz)
    max_float_por_coluna = trata_array_de_tamanhos_maximos_float(array_de_tamanhos_maximos_float, matriz)

    # Define maximo_por_coluna e maximo_por_coluna_float com base no parâmetro decimais
    if decimais is not None:
        maximo_por_coluna = [0] * len(matriz[0])
        maximo_por_coluna_float = [decimais] * len(matriz[0])
    else:
        maximo_por_coluna = [max(max(tamanhos)) for tamanhos in array_de_tamanhos_maximos]
        maximo_por_coluna_float = [max(floats) for floats in max_float_por_coluna]

    # Imprime a matriz formatada
    for linha in matriz:
        for i, valor in enumerate(linha):
            if isinstance(valor, float):
                print(f'{valor:{maximo_por_coluna[i] + maximo_por_coluna_float[i] + 1}.{maximo_por_coluna_float[i]}f}', end=' ')
            else:
                print(f'{valor:{maximo_por_coluna[i]}}', end=' ')
        print()

def copiar_matriz(matriz):
    """Retorna uma cópia da matriz."""
    return [linha[:] for linha in matriz]

def escalonar_matriz(matriz):
    """Escalona a matriz e retorna a matriz escalonada. Também retorna o número de trocas de linha."""
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
    """Calcula a determinante de uma matriz quadrada a partir de sua matriz escalonada."""
    matriz_escalonada, trocas_linhas = escalonar_matriz(matriz)
    n = len(matriz)
    
    determinante = 1
    for i in range(n):
        determinante *= matriz_escalonada[i][i]

    if trocas_linhas % 2 != 0:
        determinante *= -1
    
    return determinante

def inversa_matriz(matriz):
    """Calcula a inversa de uma matriz usando o método de escalonamento."""
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
    """Multiplica duas matrizes."""
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
    # Número de restrições e variáveis
    num_restricoes = len(A)
    num_variaveis = len(A[0])

    # Criar a tabela Simplex vazia
    tabela_simplex = []

    # Adicionar as variáveis de folga na matriz A e montar a tabela
    for i in range(num_restricoes):
        linha = A[i] + [0] * num_restricoes + [b[i]]  # Adiciona variáveis de folga e b[i]
        linha[num_variaveis + i] = 1  # Coloca 1 na posição da variável de folga
        tabela_simplex.append(linha)

    # Adicionar a linha da função objetivo com os coeficientes de c (com 0 nas variáveis de folga)
    linha_objetivo = c + [0] * (num_restricoes + 1)
    tabela_simplex.append(linha_objetivo)

    return tabela_simplex

def encontrar_pivot(tabela_simplex):
    coluna_pivot = min((valor, idx) for idx, valor in enumerate(tabela_simplex[-1][:-1]))[1]
    if all(linha[coluna_pivot] <= 0 for linha in tabela_simplex[:-1]):
        return None, None  # Sem solução viável

    linha_pivot = min((tabela_simplex[i][-1] / tabela_simplex[i][coluna_pivot], i)
                      for i in range(len(tabela_simplex) - 1)
                      if tabela_simplex[i][coluna_pivot] > 0)[1]

    return linha_pivot, coluna_pivot

def realizar_operacoes_simplex(tabela_simplex, linha_pivot, coluna_pivot):
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
    # A função objetivo está na última linha da tabela
    funcao_objetivo = tabela_simplex[-1]

    # Verificar se todos os coeficientes da função objetivo (exceto o valor da função objetivo) são >= 0
    for coeficiente in funcao_objetivo[:-1]:  # Exclui o último valor, que é o valor atual da função objetivo
        if coeficiente < 0:
            return False
    
    return True

matriz = [[-1, 1, 11], [1, 1, 27], [2, 5, 90]]
vetor_maximizacao = [-4, -6]

coeficientes = [linha[:-1] for linha in matriz]
independentes = [linha[-1] for linha in matriz]
tabela = inicializar_tabela_simplex(coeficientes, independentes, vetor_maximizacao)

while not verificar_solucao_otima(tabela):
    linha_pivot, coluna_pivot = encontrar_pivot(tabela)
    if linha_pivot is None:
        print("Problema não tem solução viável ou ilimitada.")
        break
    tabela = realizar_operacoes_simplex(tabela, linha_pivot, coluna_pivot)

print('Tabela Simplex Final:')
print_matriz(tabela, 4)
