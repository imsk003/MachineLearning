import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = 100 - (pageSpeeds + np.random.normal(0, 0.1, 1000)) * 3

plt.scatter(pageSpeeds, purchaseAmount)
plt.show()

slope, intercept, r_value, p_value, std_err = stats.linregress(pageSpeeds, purchaseAmount)

print(slope)
print(intercept)
print(r_value)
print(p_value)
print(std_err)