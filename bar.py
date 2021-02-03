import plotly_express as px 
import pandas as pd 
df  = pd.read_csv('data.csv')
fig = px.bar(df,x='Country',y='InternetUsers')
fig.show()