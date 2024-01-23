import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveRegressor


data = pd.read_csv("/Users/steveshreedhar/Desktop/Data Analyst Projects/Instagram Reach/Instagram.csv" , encoding = 'latin1')
print(data.head())

#We need to check if we have null values or not!
data.isnull().sum()

#drop null values
data = data.dropna()
data.info()


#Lets start the visulaiztions 
plt.figure(figsize = (10,10))
plt.style.use('fivethirtyeight')
plt.title("Distribution from home")
sns.distplot(data['From Home'])
plt.show()


plt.figure(figsize = (10,10))
plt.title("Distribution from Hashtags")
sns.distplot(data['From Hashtags'])
plt.show()

plt.figure(figsize = (10,10))
plt.title("Distribution from Explore")
sns.distplot(data['From Explore'])
plt.show()

plt.figure(figsize = (10,10))
plt.title("Distribution from Other")
sns.distplot(data['From Other'])
plt.show()


home = data["From Home"].sum()
hashtags = data["From Hashtags"].sum()
explore = data["From Explore"].sum()
other = data["From Other"].sum()

labels = ['From Home', 'From Hashtags', 'From Explore' , 'From Others']
values = [home,hashtags,explore,other]
fig = px.pie(data, values = values, names = labels,
            title = "Pie chart of instagram usage" , hole = 0.25)
fig.show()


#Analyzing the content andcreating the word art
text = " " . join(i for i in data.Hashtags)
stopwords = set(STOPWORDS)
wordcloud = WordCloud( stopwords = stopwords , background_color = 'white').generate(text)
plt.figure(figsize = (12,10))
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")
plt.show()


#Lets analyze the realtionships now
figure = px.scatter(data_frame = data, x = 'Impressions' , y = 'Likes', size = 'Likes', trendline = 'ols',
                   title = "Relationship between likes and impressions")
figure.show()

#Correlations
correlation = data.corr()
print(correlation["Impressions"].sort_values(ascending = False))

conversion_rate = (data["Follows"].sum() / data["Profile Visits"].sum()) * 100
print(conversion_rate)
