#1st Case Study: Annual growth of the brazilian population 1980-2016
#DataSus
import matplotlib.pyplot as plt
import numpy as np

year, population = np.loadtxt('brazilian-population.csv', delimiter = ';', unpack = True, dtype = 'int')

""" data = open('brazilian-population.csv').readlines()

year = []
population = []

for i in range(0, len(data)):
  line = data[i].split(';')

  year.append(int(line[0]))
  population.append(int(line[1])) """

plt.title('Annual growth of the brazilian population 1980-2016')
plt.xlabel('Year')
plt.ylabel('Population')

plt.bar(year, population, color = '#e4e4e4')
plt.plot(year, population, color = 'k')

plt.savefig('brazilian-population.png', dpi = 300)

plt.show()