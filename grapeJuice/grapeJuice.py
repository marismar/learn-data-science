#3rd Case Study: Import of grape juice in Brazil (2016)
#Embrapa 1970-2019
import matplotlib.pyplot as plt
import numpy as np
import csv

def getData(countries, quantities, prices, year):
  with open('grape-juice-importation.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ';')
    for row in readCSV:
      if (float(row[(year - 1970) * 2 + 2]) > 0):
        countries.append(row[1][0:3]) #get first three letters of the name of the country
        quantities.append(float(row[(year - 1970) * 2 + 2]))
        prices.append(float(row[(year - 1970) * 2 + 3]))

def showGraph(countries, quantities, prices, year):
  def autolabel(rects):
    for rect in rects:
      height = rect.get_height()
      ax.text(rect.get_x() + rect.get_width() / 2., height, '%d' % int(height), ha = 'center', va = 'bottom')

  index = np.arange(len(countries))
  fig, ax = plt.subplots()
  width = 0.4

  rects1 = ax.bar(index, quantities, width, color = 'b', align = 'center') 
  rects2 = ax.bar(index + width, prices, width, color = 'g', align = 'center')
  
  ax.set_title('Importação anual de suco de uva ' + str(year))
  ax.set_ylabel('Valor')
  ax.set_xlabel('País')

  ax.set_xticks(index + width / 2)
  ax.set_xticklabels(countries)

  ax.legend((rects1[0], rects2[0]), ('Quantidade', 'Preço'))
  
  autolabel(rects1)
  autolabel(rects2)

  plt.show()

if __name__ == '__main__':
  countries = []
  quantities = []
  prices = []
  year = 2016

  getData(countries, quantities, prices, year)
  showGraph(countries, quantities, prices, year)