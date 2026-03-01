import pandas as pd

df=pd.read_csv(r"E:\Agentic AI Material\Module 1\myFirstRepoinAgenticSystems\python-logic-assignments-pandas-intro\employee.csv")

val1=df.head()
print(f"\nFirst Five:\n\n{val1}")

val2=df.tail()
print(f"\nLast Five :\n\n {val2}")

print(f"\nDataset Info:\n\n")
df.info()

val4=df.describe()
print(f"\nDatabase Statistics:\n\n {val4}")

c1=df["name"]
print(f"\nSingle Column :\n\n{c1}")

c2=df[["name","age"]]
print(f"\nMultiple Columns using Dataframe:\n\n {c2}")

c3=df[df["age"]>30]
print(f"\nNumerical Condition based row filtering\n \n{c3}")