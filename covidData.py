import pandas as pd
import plotly.express as px

df = pd.read_csv('covid1.csv')

sc = px.scatter(df, x = "date", y = "cases", color = "country")
sc.show()
