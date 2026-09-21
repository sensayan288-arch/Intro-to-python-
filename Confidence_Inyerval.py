from scipy import stats

interval = stats.norm.interval(0.90)
print("90% interval:", interval)   # (-1.645, 1.645)
