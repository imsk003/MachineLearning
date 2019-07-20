import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

vals = np.random.normal(0, 0.5, 10000)

plt.hist(vals, 10)
plt.show()

print(np.mean(vals))
print(np.var(vals))
print(sp.skew(vals))
print(sp.kurtosis(vals))