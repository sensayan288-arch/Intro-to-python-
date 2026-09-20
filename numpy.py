import numpy as np

marks = np.array([
    [80, 70, 90],
    [60, 75, 85],
    [90, 88, 95],
    [55, 65, 70],
    [78, 82, 80]
])

# i
print("Maximum marks:", np.max(marks))

# ii
print("Minimum marks:", np.min(marks))

# iii
print("Average marks:", np.mean(marks))

# iv
print("Maximum marks subject-wise:")
for j in range(3):
    print("Subject", j + 1, ":", np.max(marks[:, j]))

# v
print("Average marks subject-wise:")
for j in range(3):
    print("Subject", j + 1, ":", np.mean(marks[:, j]))
