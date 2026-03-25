import pandas as pd
import plotly.express as px

df=pd.read_csv(r"E:\Agentic AI Material\Module 1\myFirstRepoinAgenticSystems\eda-checklist\iris.csv")
print(df.shape)
print(df.head())
print(df.columns)
df.info()
print(df.isnull().sum())

fig=px.histogram(
  df,
  x="petal_length",
  color="species",
  color_discrete_sequence=["blue","orange","green"]
)
fig.show()

fig1=px.box(
  df,
  y="sepal_width",
  x="species",
  color="species",
  color_discrete_sequence=["blue","orange","green"]
)
fig1.show()

fig2=px.scatter(
  df,
  x="petal_length",
  y="petal_width",
  color="species",
  color_discrete_sequence=["blue","orange","green"]
)
fig2.show()

