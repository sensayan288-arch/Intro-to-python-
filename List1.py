
names = []

while len(names) < 10:
    name = input("Enter student name: ")
    if name not in names:
        names.append(name)
    else:
        print("Duplicate name not allowed!")


marks = []

for i in range(10):
    mark = int(input("Enter marks of " + names[i] + ": "))
    marks.append(mark)
max_mark = max(marks)
min_mark = min(marks)

max_student = names[marks.index(max_mark)]
min_student = names[marks.index(min_mark)]

print("\nStudent with highest marks:")
print(max_student, "=", max_mark)

print("\nStudent with lowest marks:")
print(min_student, "=", min_mark)
