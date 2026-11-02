import pandas as pd

employees = {
    "employee_id": [101, 102, 103, 104, 105],
    "employee_name": ["Ayan", "Riya", "Sima", "Karan", "Binita"],
    "department": ["IT", "HR", "Sales", "IT", "Finance"],
    "salary": [35000, 42000, 39000, 50000, 45000]
}

employee_df = pd.DataFrame(employees)

print(employee_df.head(2))
print(employee_df.tail(2))
print(employee_df.loc[employee_df["salary"].idxmax()])

students = {
    "roll": [1, 2, 3, 4, 5],
    "name": ["Ayan", "Ria", "Sima", "Kaju", "Binita"],
    "department": ["CSE", None, "ECE", None, "IT"],
    "marks": [90, 80, None, 85, 25]
}

student_df = pd.DataFrame(students)

print(student_df.isnull().sum())

student_df["department"] = student_df["department"].fillna("SSE")

student_df.loc[student_df["name"] == "Kaju", "department"] = "VLSI"

student_df = student_df.dropna(subset=["marks"])

print(student_df)
