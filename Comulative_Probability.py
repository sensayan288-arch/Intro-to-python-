from scipy import stats

p = stats.norm.cdf(1.5)
print("P(Z < 1.5) =", p)   # ≈ 0.9332
