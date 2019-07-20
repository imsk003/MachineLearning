import numpy as np
from scipy import stats

incomes = np.random.normal(20000, 15000, 10000)
print(np.mean(incomes))

print(np.median(incomes))

ages = np.random.randint(18, high=90, size=500)
print(stats.mode(ages))