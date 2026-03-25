import pandas as pd
import plotly.express as px



data={
  "Epoch":[1,2,3,4,5,6,7,8,9,10 ],
  "Loss":[0.98,0.95,0.85,0.79,0.65,0.52,0.44,0.39,0.26,0.25]
}
df=pd.DataFrame(data)
fig=px.line(
  df,
  x="Epoch",
  y="Loss",
  title="Training Loss Over Epochs"
)
fig.add_annotation(
  x=9,
  y=0.26,
  text="This is where loss stabilzes",
  showarrow=True,
  arrowhead=6
)
fig.show()
