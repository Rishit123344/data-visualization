import plotly.express as px
import pandas as pd 
df = pd.read_csv('line_chart.csv')
fig = px.line(df,x='Year',y='Per capita income',color='Country',title='Per capita income')
fig.show()