from scipy import stats


marks = [18, 15, 12, 20, 17]
t, p = stats.ttest_1samp(marks, 50)
print("t =", t, " p =", p)

if p < 0.05:
    print("Reject H0 — mean is significantly different from 50")
else:
    print("Fail to reject H0")

marks_b = [15, 18, 20, 17, 16]
marks_g = [19, 21, 18, 20, 22]
t2, p2 = stats.ttest_ind(marks_b, marks_g)
print("t =", t2, " p =", p2)
