matriz = [
    [1, 2, 3],
    [16, 8,7],
    [4,6,7],
]

def dividir_lista(lista, tamanho):
    return [lista[i:i + tamanho] for i in range(0, len(lista), tamanho)]

def pega_tamanho_maximo(matriz):
    array_de_tamanhos_maximos = []
    array_de_tamanhos_maximos_float = []

    # percorre as linhas da matriz para pegar o tamanho máximo de cada coluna
    for i in range(len(matriz[0])):
        for linha in matriz:
            array_de_tamanhos_maximos.append(len(str(linha[i]).split('.')[0]))
            array_de_tamanhos_maximos_float.append(len(str(linha[i]).split('.')))
    
    array_de_tamanhos_maximos = dividir_lista(array_de_tamanhos_maximos, len(matriz[0]))
    
    return array_de_tamanhos_maximos, array_de_tamanhos_maximos_float

def trata_array_de_tamanhos_maximos_float(array_de_tamanhos_maximos_float):
    max_float_por_coluna = []

    if max(array_de_tamanhos_maximos_float) > 1:
        for i in range(len(matriz[0])):
            for linha in matriz:
                if len(str(linha[i]).split('.')) > 1:
                    max_float_por_coluna.append(len(str(linha[i]).split('.')[1]))
                else:
                    max_float_por_coluna.append(0)
    max_float_por_coluna = dividir_lista(max_float_por_coluna, len(matriz[0]))
    return max_float_por_coluna

def maximos_por_coluna(array_de_tamanhos_maximos, max_float_por_coluna):
    maximo_por_coluna, maximo_por_coluna_float = [], []

    for i in array_de_tamanhos_maximos:
        maximo_por_coluna.append(max(i))

    for i in max_float_por_coluna:
        maximo_por_coluna_float.append(max(i))
    return maximo_por_coluna, maximo_por_coluna_float


def print_matriz(matriz, maximo_por_coluna, maximo_por_coluna_float):

    if maximo_por_coluna_float == []:
        for linha in matriz:
            for i in range(len(linha)):
                print(f'{linha[i]:{maximo_por_coluna[i]}}', end=' ')
            print()
    else:
        for linha in matriz:
            for i in range(len(linha)):
                if maximo_por_coluna_float[i] > 4:
                    maximo_por_coluna_float[i] = 4
                print(f'{linha[i]:{maximo_por_coluna[i] + maximo_por_coluna_float[i] + 1}.{maximo_por_coluna_float[i]}f}', end=' ')
            print()

# TODO função para calcular a inversa,
# para calcular o produto de matrizes,
# executar o simplex matricial,s
# reproduzir o tableau

def calcular_determinante_by_upper_triangle(matriz):
    tamanho = len(matriz)
    copia = matriz

    for i in range(tamanho):
        for j in range(i+1, tamanho):
            if copia[i][i] == 0:
                continue
            fator = copia[j][i] / copia[i][i]
            for k in range(tamanho):
                copia[j][k] = copia[j][k] - fator * copia[i][k]

    determinante = 1
    for i in range(tamanho):
        determinante *= copia[i][i]

    return determinante, copia

def inverter_a_matriz(matriz, determinante):
    matriz_inversa = []
    for i in range(len(matriz)):
        linha = []
        for j in range(len(matriz)):
            linha.append(matriz[j][i] / determinante)
        matriz_inversa.append(linha)
    return matriz_inversa


def main(matriz):
    array_de_tamanhos_maximos, array_de_tamanhos_maximos_float = pega_tamanho_maximo(matriz)
    max_float_por_coluna = trata_array_de_tamanhos_maximos_float(array_de_tamanhos_maximos_float)
    maximo_por_coluna, maximo_por_coluna_float = maximos_por_coluna(array_de_tamanhos_maximos, max_float_por_coluna)
    print_matriz(matriz, maximo_por_coluna, maximo_por_coluna_float)
    determinante, m_escalonada = calcular_determinante_by_upper_triangle(matriz)
    print('\nDeterminante:', determinante)

    array_de_tamanhos_maximos, array_de_tamanhos_maximos_float = pega_tamanho_maximo(m_escalonada)
    max_float_por_coluna = trata_array_de_tamanhos_maximos_float(array_de_tamanhos_maximos_float)
    maximo_por_coluna, maximo_por_coluna_float = maximos_por_coluna(array_de_tamanhos_maximos, max_float_por_coluna)
    
    print('\nmatriz escalonada:')
    print_matriz(m_escalonada, maximo_por_coluna, maximo_por_coluna_float)
   
    matriz_inversa = inverter_a_matriz(matriz, determinante)
    print('\nmatriz inversa:')
    array_de_tamanhos_maximos, array_de_tamanhos_maximos_float = pega_tamanho_maximo(matriz_inversa)
    max_float_por_coluna = trata_array_de_tamanhos_maximos_float(array_de_tamanhos_maximos_float)
    print_matriz(matriz_inversa, maximo_por_coluna, maximo_por_coluna_float)

main(matriz)