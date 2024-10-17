tabela_parsing = {
    'S': {'a': 'S->AB', 'b': 'S->AB', 'ε': 'S->AB'},
    'A': {'a': 'A->aA', 'b': 'A->ε', 'ε': 'A->ε'},
    'B': {'a': 'ERRO', 'b': 'B->bB', 'ε': 'B->ε'}
}

producoes = {
    'S->AB': ['A', 'B'],
    'A->aA': ['a', 'A'],
    'A->ε': ['ε'],
    'B->bB': ['b', 'B'],
    'B->ε': ['ε']
}

def parser(entrada):
    pilha = ['S', 'ε']
    entrada += 'ε'
    
    print(f'{"Pilha":<10} {"Entrada":<10} {"Ação":<20}')
    while len(pilha) > 0:
        topo_pilha = pilha.pop(0)
        proximo_entrada = entrada[0]

        if topo_pilha == 'ε' and proximo_entrada == 'ε':
            print(f'{topo_pilha:<10} {entrada:<10} {"Aceitou"}')
            break

        if topo_pilha in tabela_parsing and proximo_entrada in tabela_parsing[topo_pilha]:
            acao = tabela_parsing[topo_pilha][proximo_entrada]
            if acao == 'ERRO':
                print(f'{topo_pilha:<10} {entrada:<10} {"Erro"}')
                break
            else:
                print(f'{topo_pilha:<10} {entrada:<10} {acao}')
                producao = producoes[acao]
                if producao[0] != 'ε':
                    pilha = producao + pilha
        elif topo_pilha == proximo_entrada:
            entrada = entrada[1:]
            print(f'{topo_pilha:<10} {entrada:<10} {"Casa " + topo_pilha}')

        else:
            print(f'{topo_pilha:<10} {entrada:<10} {"Erro"}')
            break

entrada = 'ababb'
parser(entrada)