import pandas
import plotly.express as px
df = pandas.read_csv(r"C:\Users\rajuv\Desktop\python practice\Copy+of+data+-+data.csv")
fig = px.scatter(df,x = "date",y = "cases")
fig.show()