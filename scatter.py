import plotly_express as px 
import pandas as pd 
df = pd.read_csv('data.csv')
fig = px.scatter(df,x='Population',y='Per capita',size='Percentage',color='Country',size_max=60)
fig.show()