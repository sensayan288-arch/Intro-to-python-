EMP = {
    "E1": {
        "Name": "Sarthak Sen",
        "Designation": "Officer",
        "Department": "Software Engineering",
        "Salary": 80000
    },
    "E2": {
        "Name": "Srestho Majumder",
        "Designation": "Officer",
        "Department": "Artificial Intelligence",
        "Salary": 77000
    },
    "E3": {
        "Name": "ANkush Roy",
        "Designation": "Intern",
        "Department": "Software Engineering",
        "Salary": 22000
    },
    "E4": {
        "Name": "Avik Mondal",
        "Designation": "Officer",
        "Department": "Machine Learning",
        "Salary": 80000
    },
    "E5": {
        "Name": "Ayush Mishra",
        "Designation": "Manager",
        "Department": "Software Engineering",
        "Salary": 80000
    }
}
________
print(EMP.get("E1"))
_________
print(EMP.get("E4").get("Department"))
_________
max_emp = max(EMP, key=lambda x: EMP[x]["Salary"])
print(max_emp)
___________
EMP.update({
    "E6": {
        "Name": "Rahul",
        "Designation": "Intern",
        "Department": "Software Engineering",
        "Salary": 25000
    }
})
