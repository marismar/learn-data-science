import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

plt.title('Bar Graph')
plt.xlabel('X')
plt.ylabel('Y')

plt.bar(x1, y1, label = '1st Group')
plt.bar(x2, y2, label = '2nd Group')

plt.show()