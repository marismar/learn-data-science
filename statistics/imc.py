import matplotlib.pyplot as plt
import numpy as np
from random import uniform, randint

def createRandomData():
  data = open('height-weight-force.csv', 'w+', encoding = 'UTF-8')
  
  info = []
  info.extend(str(uniform(1.50, 2.20)) + ';' + str(uniform(50, 120)) + ';' + 
              str(uniform(1, 10)) + '\n' for i in range(0, 140))
  
  data.writelines(info)
  data.close()


def tabulatedImc(imc):
  if imc < 16:
    return str(imc) + ': Magreza grave'
  elif imc < 17:
    return str(imc) + ': Magreza moderada'
  elif imc < 18.5:
    return str(imc) + ': Magreza leve'
  elif imc < 25:
    return str(imc) + ': Saudável'
  elif imc < 30:
    return str(imc) + ': Sobrepeso'
  elif imc < 35:
    return str(imc) + ': Obesidade grau I'
  elif imc < 40:
    return str(imc) + ': Obesidade grau II (severa)'
  else:
    return str(imc) + ': Obesidade grau III (mórbida)'


if __name__ == '__main__':
  createRandomData()

  height, weight, force = np.loadtxt('height-weight-force.csv',
                                     delimiter = ';',
                                     unpack = True,
                                     dtype = 'float')

  imc = weight / height ** 2

  print('Min: ', tabulatedImc(np.amin(imc)))
  print('Max: ', tabulatedImc(np.amax(imc)))
  print('Max - Min: ', tabulatedImc(np.ptp(imc)))

  print('Média: ', tabulatedImc(np.median(imc)))
  print('Média por força: ', tabulatedImc(np.average(imc)))
  print('Média aritmética: ', tabulatedImc(np.mean(imc)))
  
  print('Desvio padrão: ', tabulatedImc(np.std(imc)))
  print('Variância: ', tabulatedImc(np.var(imc)))

  print('IMC médio do 1º Percentil: ', tabulatedImc(np.median(np.percentile(imc, q = range(0, 25)))))
  print('IMC médio do 2º Percentil: ', tabulatedImc(np.median(np.percentile(imc, q = range(26, 50)))))
  print('IMC médio do 3º Percentil: ', tabulatedImc(np.median(np.percentile(imc, q = range(51, 75)))))
  print('IMC médio do 4º Percentil: ', tabulatedImc(np.median(np.percentile(imc, q = range(76, 100)))))

  values = []
  index = [1, 2, 3, 4]

  values.append(np.median(np.percentile(imc, q = range(0, 25))))
  values.append(np.median(np.percentile(imc, q = range(26, 50))))
  values.append(np.median(np.percentile(imc, q = range(51, 75))))
  values.append(np.median(np.percentile(imc, q = range(76, 100))))

  plt.title('Percentil dos IMC da população')  
  plt.ylabel('Valor')
  plt.xlabel('Percentil')
  
  plt.plot(index, values)
  plt.show()