def primeiro(simbolo, producoes, conjunto_primeiro):
    if simbolo in conjunto_primeiro:
        return conjunto_primeiro[simbolo]
    conjunto_primeiro[simbolo] = set()

    if simbolo.isLower() or simbolo == 'ε':
        conjunto_primeiro[simbolo].add(simbolo)

    else:
        for producao in producoes[simbolo]:
            if producao[0] == 'ε':
                conjunto_primeiro[simbolo].add('ε')
            else:
                for s in producao:
                    conjunto_primeiro[simbolo].update(primeiro(s, producoes, conjunto_primeiro))
                    if 'ε' not in conjunto_primeiro[s]:
                        break
                    else:
                        conjunto_primeiro[simbolo].add('ε')
            
    return conjunto_primeiro[simbolo]

def seguinte(simbolo, producoes, conjunto_primeiro, conjunto_seguinte, simbolo_inicial):
    if simbolo in conjunto_seguinte:
        return conjunto_seguinte[simbolo]
    conjunto_seguinte[simbolo] = set()

    if simbolo == simbolo_inicial:
        conjunto_seguinte[simbolo].add('$')

    for nao_terminal, lista_producoes in producoes.items():
        for producao in lista_producoes:
            if simbolo in producao:
                pos = producao.index(simbolo)

                if pos < len(producao) - 1:
                    proximo_simbolo = producao[pos + 1]
                    conjunto_seguinte[simbolo].update(seguinte(proximo_simbolo, producoes, conjunto_primeiro, conjunto_seguinte, simbolo_inicial))
                    if 'ε' in primeiro(proximo_simbolo, producoes, conjunto_primeiro):
                        conjunto_seguinte[simbolo].update(seguinte(nao_terminal, producoes, conjunto_primeiro, conjunto_seguinte, simbolo_inicial))
                else:
                    if nao_terminal != simbolo:
                        conjunto_seguinte[simbolo].update(seguinte(nao_terminal, producoes, conjunto_primeiro, conjunto_seguinte, simbolo_inicial))

    return conjunto_seguinte[simbolo]

def sincronizacao(simbolo, producoes, conjunto_primeiro, conjunto_seguinte, simbolos_nivel_superior):
    conjunto_sincronizacao = set()

    conjunto_sincronizacao.update(conjunto_seguinte[simbolo])

    conjunto_sincronizacao.update(simbolos_nivel_superior)

    conjunto_sincronizacao.update(primeiro(simbolo, producoes, conjunto_primeiro))

    return conjunto_sincronizacao