import pandas as pd

salary = pd.Series([25000, 30000, 28000, 35000, 40000, 32000, 45000, 38000, 27000, 50000],
                   index=["Ayan", "Riya", "Sima", "Karan", "Binita", "Rahul", "Priya", "Arjun", "Mina", "Rohan"])

print(salary)
print("Average salary:", salary.mean())

products = {
    "product_name": ["Pen", "Notebook", "Bag", "Bottle", "Pencil", "Calculator"],
    "price": [10, 45, 250, 60, 5, 180]
}

df = pd.DataFrame(products)

print("Average price:", df["price"].mean())
print(df[df["price"] > df["price"].mean()])
print(df[df["price"] > 50])
