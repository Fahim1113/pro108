import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")

avrageRating = list(df["Avg Rating"])

fig = ff.create_distplot([avrageRating], ["bell-curve"])
fig.show()