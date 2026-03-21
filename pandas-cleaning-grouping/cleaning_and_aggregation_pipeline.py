# 🔹 Sample Data (5–10 Rows)

import pandas as pd
import numpy as np

# Creating sample dataset
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

print(df)

print(df.isnull())
print(df.isnull().sum())

df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
print(df)

df=df.drop("Temporary_Notes", axis=1)
print(df)

df=df.rename(columns={"Salary":"Annual_Salary"})
print(df)

val1=df.groupby("Department")["Annual_Salary"].mean()
print(val1)

val2=df.groupby("Department")["Employee"].count()
print(val2)

print("\n\nFinal Table:\n\n")
print(df)

print("Super Final Table    ")