emp = ("Ayush","Bitan","Chetak","Diya","Emran","Fajal","Sunio","Gian","Issac","Doreamon","Krish","Ayush","Manik","Nitin","Dekisugi","Pritha","Queue","Rishi","Sarthak","Tiya")
for x in emp:
    print(x,emp.count(x))
emp1=list(emp)
for x in emp1:
    if emp1.count(x)>1:
        emp1.remove(x)
emp = tuple(emp1)
print("*******after removal of duplicates******* ")
for x in emp:
    print(x,emp.count(x))
check = input("enter a name to check if present or not")
if check in emp:
    print("present")
else:
    print("not present")
print("*****sorting tuple******")
print(sorted(emp))
