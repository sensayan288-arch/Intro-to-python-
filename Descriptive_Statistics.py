from scipy import stats
import numpy as np

marks = [18, 16, 12, 17, 15, 19, 20, 16, 18, 15]


print(stats.describe(marks))

print("Median:", np.median(marks))
print("Mode:", stats.mode(marks, keepdims=True))
print("Std Dev:", np.std(marks, ddof=1))
