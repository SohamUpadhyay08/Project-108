import pandas as pd
import plotly.figure_factory as ff
import csv

df = pd.read_csv("mobiles.csv")
graph = ff.create_distplot([df["Avg Rating"].tolist()],["Rating"],show_hist=True)
graph.show()