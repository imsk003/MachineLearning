import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(2)

pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50, 10, 1000) / pageSpeeds

plt.scatter(pageSpeeds, purchaseAmount)
plt.show()