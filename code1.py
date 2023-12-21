import matplotlib.pyplot as plt

data = [25, 45, 55, 100, 155]
kategori = ['A', 'B', 'C', 'D', 'E']

plt.bar(kategori, data)
plt.grid()

plt.show()