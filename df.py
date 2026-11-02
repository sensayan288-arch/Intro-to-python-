import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

print(df.head())

df.drop_duplicates(inplace=True)
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

female_passengers = df[(df["Fare"] > 270) & (df["Sex"] == "female")]
print(female_passengers)

first_class = df[df["Pclass"] == 1]
print(first_class.describe(include="all"))

df.drop_duplicates(inplace=True)
print(df)
