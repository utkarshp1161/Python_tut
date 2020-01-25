# read a csv file
import pandas as pd 


df=pd.read_csv('macro_input.csv')
print (df.head())


import plotly.express as px
import plotly


#plot in 2d:
#df2=df['R1','R2']
#fig = px.scatter(df, x= df['R1'],y= df['R2'])
#plotly.offline.plot(fig, "raw_plot_post_preprocessing.html")

#plot in 3d

fig = px.scatter_3d(df, x='R1', y='R2', z='R3')
plotly.offline.plot(fig, "3d.html")