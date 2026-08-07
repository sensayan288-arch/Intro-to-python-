fruits = {"Apple","Mango","Guava","Banana","Litchi"}
summer_fruits = {"Mango","Litchi","Jackfruit","Watermelon"}
winter_fruits = {"Kiwi","Apple","Orange","Guava","Strawberry"}
print("Fruits:",fruits)
print(" Summer Fruits:",summer_fruits)
print("Winter Fruits:",winter_fruits)
print("fruit in fruits and winter_fruits",fruits.union(winter_fruits))
print("fruit in summer_fruits but not in fruits",summer_fruits.difference(fruits))
print("fruit in summer_fruits and winter_fruits",summer_fruits.intersection(winter_fruits))
if "Orange" in fruits:
    print("Orange Exists")
else:
    print("Orange Doesn't exist")
