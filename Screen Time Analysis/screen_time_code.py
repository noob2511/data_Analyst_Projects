import pandas as pd
import numpy as np
import plotly.express  as px
import plotly.graph_objects as go

data = pd.read_csv('/Users/steveshreedhar/Desktop/Data Analyst Projects/Screen Time /screentime.csv')
print(data.head())
print('****************')
print(data.describe())
print(data.isnull().sum())

#lets create a bar graph for distributions

fig = px.bar(data_frame = data,
            x = "Date",
            y = "Usage",
            color = "App",
            title = "Usage")
fig.show()


fig = px.bar(data_frame = data,
            x = "Date",
            y = "Notifications",
            color = "App",
            title = "Notifications")
fig.show()


fig = px.bar(data_frame = data,
            x = "Date",
            y = "Times opened",
            color = "App",
            title = "Time opened")
fig.show()
