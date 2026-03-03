import pandas as pd


df = pd.read_csv(r"E:\Agentic AI Material\Module 1\myFirstRepoinAgenticSystems\python-logic-assignments-pandas-selection-and-filtering\marks.csv")
print(df["Name"])

ndf=df[["Name","Score","Category"]]
print(ndf)

print(df.iloc[0:3])

ex1=ndf.copy()
ex1.index=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
print(ex1.loc["G":"M"])

condition1=df[df["Score"]>85]
print(condition1)

condition2 =df[(df["Score"]>85)&(df["Passed"]==True)].sort_values(["Score"],ascending=False)
print("High Performing Students:")
print(condition2[["Name","Score"]])



