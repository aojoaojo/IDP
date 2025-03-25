def main():
    palavra = str(input('insira sua palavra: '))
    if is_palavra_valida(palavra):
        return
    zeros, uns = checa_zeros_e_uns(palavra)
    if (zeros % 2 == 0) and (uns % 2 == 0):
        print('Palavra válida')
    else:
        print('Palavra inválida')

def checa_zeros_e_uns(palavra):
    quantidade_de_0s = 0
    quantidade_de_1s = 0
    for letra in palavra:
        if (letra == '0'):
            quantidade_de_0s += 1
        else:
            quantidade_de_1s += 1    
    return quantidade_de_0s, quantidade_de_1s


def is_palavra_valida(palavra):
    for letra in palavra:
        print(letra, end=' ')
        if (letra not in ('0', '1')):
            print("Palavra inválida, este alfabeto só aceita 0's e 1's")
            return 1
    return 0

if __name__ == '__main__':
    main()