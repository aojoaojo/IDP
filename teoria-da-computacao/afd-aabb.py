def estado1(indice_letra, palavra):
    print('Estado 1')
    if indice_letra == len(palavra):
        print('Palavra aceita')
        return True
    elif palavra[indice_letra] == 'a':
        return estado2(indice_letra+1, palavra)
    elif palavra[indice_letra] == 'b':
        return estado4(indice_letra+1, palavra)

def estado2(indice_letra, palavra):
    print('Estado 2')
    if indice_letra == len(palavra):
        print('Palavra negada')
        return False
    elif palavra[indice_letra] == 'b':
        return estado3(indice_letra+1, palavra)
    elif palavra[indice_letra] == 'a':
        return estado1(indice_letra+1, palavra)
    
def estado3(indice_letra, palavra):
    print('Estado 3')
    if indice_letra == len(palavra):    
        print('Palavra negada')
        return False
    elif palavra[indice_letra] == 'b':
        return estado2(indice_letra+1, palavra)
    elif palavra[indice_letra] == 'a':
        return estado4(indice_letra+1, palavra)

def estado4(indice_letra, palavra):
    print('Estado 4')
    if indice_letra == len(palavra):    
        print('Palavra negada')
        return False
    elif palavra[indice_letra] == 'a':
        return estado3(indice_letra+1, palavra)
    elif palavra[indice_letra] == 'b':
        return estado1(indice_letra+1, palavra)

def main():
    palavra = input('Insira uma palavra do alfabeto {a, b}: ')
    estado1(0, palavra)

if __name__ == '__main__':
    main()