import pandas as pd
import plotly.express as px
import plotly

df=pd.read_csv('bar_chart.csv')

fig=px.bar(df,x=df['ion'],y=df['Relative response'])
plotly.offline.plot(fig, "3d.html")