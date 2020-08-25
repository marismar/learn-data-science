import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [200, 25, 400, 3300, 100]

plt.title('Scartterplot')
plt.xlabel('X')
plt.ylabel('Y')

plt.plot(x, y, c = '#000000', linestyle = ':') 
plt.scatter(x, y, label = 'points', color = 'r', marker = '.', s = z)

plt.legend()
plt.show()

plt.savefig('scartterplot.png', dpi = 300)  #save the figure at current directory