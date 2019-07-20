import matplotlib.pyplot as plt

values = [12, 55, 4, 32, 14]
colors = ['r', 'g', 'b', 'c', 'm']
labels = ['India', 'US', 'UK', 'Russia', 'Australia']
explode = [0, 0, 0.2, 0, 0]

plt.pie(values, colors = colors, labels = labels, explode = explode)
plt.title("Student Location")
plt.show()