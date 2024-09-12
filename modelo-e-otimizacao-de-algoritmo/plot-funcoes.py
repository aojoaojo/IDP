
def input_de_equacao():
  # equacao1 = input('Digite a primeira equação do sistema: ')
  # equacao2 = input('Digite a segunda equação do sistema: ')
  # return equacao1, equacao2 
  equacao1 = '-x - 2y = -4'
  equacao2 = '-x + y = -1'

  x = equacao1[:(idx:=equacao1.index('x'))]
  y = equacao1[idx+1:(idy:=equacao1.index('y'))]
  result = equacao1[equacao1.index('=') + 1:]
  x2 = equacao2[:(idx:=equacao2.index('x'))]
  y2 = equacao2[idx+1:(idy:=equacao2.index('y'))]
  result2 = equacao2[equacao2.index('=') + 1:]
  numeros = [x, y, result]
  numeros2 = [x2, y2, result2]
  numeros = tratamento_de_numero(numeros)
  numeros2 = tratamento_de_numero(numeros2)
  cramer(numeros, numeros2)

def tratamento_de_numero(numeros):
  for i in range(len(numeros)):
    if numeros[i] == '-':
      numeros[i] = '-1'
    elif numeros[i] == ' + ':
      numeros[i] = '1'

    numeros[i] = int(numeros[i].replace(' ', ''))

  return numeros

def cramer(numeros1, numeros2):

  det1 = (numeros1[0]*numeros2[1]) - (numeros1[1] * numeros2[0])
  det2 = (numeros1[2]*numeros2[1]) - (numeros1[1] * numeros2[2])
  det3 = (numeros1[0]*numeros2[2]) - (numeros1[2] * numeros2[0])

  x = det2/det1
  y = det3/det1

  print('x:', x)
  print('y:', y)

  plot_sistema([x, y], [numeros1[2], numeros2[2]], numeros1, numeros2)

def plot_sistema(x, y, numeros1, numeros2):
  import matplotlib.pyplot as plt

  plt.plot(x, y, label='x + 2y = 4')
  plt.plot(x, y, label='x - y = 1')
  plt.legend()
  plt.show()

input_de_equacao()

