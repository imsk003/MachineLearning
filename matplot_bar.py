import matplotlib.pyplot as plt

values = [12, 55, 4, 32, 14]
colors = ['r', 'g', 'b', 'c', 'm']

plt.bar(range(0, 5), values, color = colors)
plt.title("Student Location")
plt.show()