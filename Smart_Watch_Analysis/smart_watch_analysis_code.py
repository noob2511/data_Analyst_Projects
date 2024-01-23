import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


data = pd.read_csv("/Users/steveshreedhar/Desktop/Data Analyst Projects/Smart Watch Project/dailyActivity_merged.csv")
print(data.head())

#Now we need to check if the data fields we have are null or not
print(data.isnull().sum())
#The data dosent contain any null values
#Lets print the data information
print(data.info())

#lets change the object data type to a date datatype of Activity Date
data["ActivityDate"] = pd.to_datetime(data["ActivityDate"], 
                                      format="%m/%d/%Y")
print(data.info())

data["TotalMinutes"] = data["VeryActiveMinutes"]+ data["FairlyActiveMinutes"]+data["SedentaryMinutes"]
print(data["TotalMinutes"].sample(5))

#lets see the descriptive statistics (involves mean, median, mode, variance,  standard variation etc.)
print(data.describe())

#Lets analyze the data
figure = px.scatter(data_frame = data, x="Calories",
                    y="TotalSteps", size="VeryActiveMinutes", 
                    trendline="ols", 
                    title="Relationship between Calories & Total Steps")
figure.show()

fig = go.Figure()
fig.add_trace(go.Bar(
    x=data["Day"],
    y=data["VeryActiveMinutes"],
    name='Very Active',
    marker_color='purple'
))
fig.add_trace(go.Bar(
    x=data["Day"],
    y=data["FairlyActiveMinutes"],
    name='Fairly Active',
    marker_color='green'
))
fig.add_trace(go.Bar(
    x=data["Day"],
    y=data["LightlyActiveMinutes"],
    name='Lightly Active',
    marker_color='pink'
))
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()

data["Day"] = data["ActivityDate"].dt.day_name()
print(data["Day"].head())
