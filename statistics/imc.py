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

  print('Media: ', tabulatedImc(np.median(imc)))
  print('Media por força: ', tabulatedImc(np.average(imc)))
  print('Media aritmetica: ', tabulatedImc(np.mean(imc)))
  
  print('Desvio padrao: ', tabulatedImc(np.std(imc)))
  print('Variancia: ', tabulatedImc(np.var(imc)))