from scipy import stats
import numpy as np

marks = [18, 16, 12, 17, 15, 19, 20, 16, 18, 15]

print(stats.describe(marks))
print("Median:", np.median(marks))
print("Mode:", stats.mode(marks, keepdims=True))
print("Std Dev:", np.std(marks, ddof=1))

print("Standard normal probability:", stats.norm.cdf(1.5))
print("Normal distribution interval:", stats.norm.interval(0.40))

marks = [18, 15, 12, 20, 17]
t, p = stats.ttest_1samp(marks, 50)
print("One-sample t-test:", t, p)

if p < 0.05:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")

marks_b = [12, 17, 16, 13, 19]
marks_g = [13, 13, 16, 20, 19]

t, p = stats.ttest_ind(marks_b, marks_g)
print("Independent t-test:", t, p)

if p < 0.05:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")
