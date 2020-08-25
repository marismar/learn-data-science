#2nd Case Study: Comparing genomes
import matplotlib.pyplot as plt
from itertools import permutations

inputData = open('bacteria.fasta').read().replace('\n','')
outputData = open('bacteria.html', 'w')
genomeCounter = {}

for perm in permutations(['A','A','T','T','C','C','G','G'], 2):
  genomeCounter.setdefault(perm[0] + perm[1], 0)

for i in range(0,len(inputData) - 1):
  genomeCounter[inputData[i] + inputData[i+1]] += 1

aux = 1 #auxiliar counter
for key, value in genomeCounter.items():
  outputData.write(
      "<div style = 'width:100px; border:1px solid #111; height:100px; float:left;\
      background-color:rgba(0, 0, 255, " + str(value/max(genomeCounter.values())) + ")'>" + key + \
      "</div>\n"
    )

  if aux % 4 == 0:
    outputData.write("<div style = 'clear:both'></div>\n")
  aux += 1
  
outputData.close()