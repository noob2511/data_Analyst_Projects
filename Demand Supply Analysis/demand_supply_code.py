import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv("/Users/steveshreedhar/Desktop/Data Analyst Projects/Demand and Supply Analysis/rides.csv")
print(data.head())

#Check if the data set has null values or not
print(data.isnull().sum())

# we can see it ha 54 null rows lets drop those
data.dropna()

# lets analyze the relationship between number of drivers per hour to number of rides per hour
demand = data['Riders Active Per Hour']
supply = data['Drivers Active Per Hour']

figure = px.scatter(data,
                   x = "Drivers Active Per Hour",
                   y = "Riders Active Per Hour",
                   trendline = "ols",
                   title ="Demand Supply Analysis")
figure.update_layout(xaxis_title = "Drivers(Supply)",
                    yaxis_title = "Riders(Demand)")
figure.show()

#now lets calcualte the elasticity between the drivers and riders

avg_demand= data['Riders Active Per Hour'].mean()
avg_supply  = data['Drivers Active Per Hour'].mean()
pct_change_demand = (max(data['Riders Active Per Hour']) - min(data['Riders Active Per Hour'])) / avg_demand * 100
pct_change_supply = (max(data['Drivers Active Per Hour']) - min(data['Drivers Active Per Hour'])) / avg_supply * 100

elasticity = pct_change_demand/pct_change_supply

print("Elasticity is: {:.2f}". format(elasticity))



#lets calculate the supply chain ratio
data['Supply Ratio'] = data['Rides Completed'] / data['Drivers Active Per Hour']

print(data.head())

#lets analyze the supply chain ratio

fig = go.Figure()
fig.add_trace(go.Scatter( x = data['Drivers Active Per Hour'],
                        y = data['Supply Ratio'] , mode = 'markers'))
fig.update_layout(
    title = "Analyzing the supply chain ratio",
    xaxis_title = 'Driver activity',
    yaxis_title = 'Supply Ratio')
fig.show()
