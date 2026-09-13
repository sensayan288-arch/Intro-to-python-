
marks = [
    [80, 70, 90],
    [60, 75, 85],
    [90, 88, 95],
    [55, 65, 70],
    [78, 82, 80]
]

# i
print("Maximum marks:", max(max(row) for row in marks))

# ii
print("Minimum marks:", min(min(row) for row in marks))

# iii
total = sum(sum(row) for row in marks)
average = total / 15
print("Average marks:", average)

# iv
print("Maximum marks subject-wise:")
for j in range(3):
    maximum = max(marks[i][j] for i in range(5))
    print("Subject", j + 1, ":", maximum)

#v
print("Average marks subject-wise:")
for j in range(3):
    total = sum(marks[i][j] for i in range(5))
    average = total / 5
    print("Subject", j + 1, ":", average)
