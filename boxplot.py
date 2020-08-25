import matplotlib.pyplot as plt
import random

arr = []
arr.extend(random.randint(0, 1000) for i in range(10))

plt.boxplot(arr)
plt.show()