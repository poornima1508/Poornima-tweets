import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Title of the app
st.title('Airline Tweets Sentiment Analysis')

# Load the dataset
tweets = pd.read_csv('https://raw.githubusercontent.com/poornima1508/Poornima-tweets/refs/heads/main/Tweets.csv')

# Display the dataset in the app
st.subheader('Preview of the Dataset')
st.dataframe(tweets.head())

# Sentiment counts pie chart
st.subheader('Tweet Sentiments Breakdown')

# Calculate sentiment counts
sentiment_counts = tweets['airline_sentiment'].value_counts().reset_index()
sentiment_counts.columns = ['airline_sentiment', 'count']

# Create and display the pie chart
fig = px.pie(sentiment_counts,
             values='count',
             names='airline_sentiment',
             title='Count of Tweets by Sentiment')
st.plotly_chart(fig)

# Tweet counts by airlines (bar plot)
st.subheader('Tweet Counts by Airline')

# Calculate tweet counts by airlines
airline_counts = tweets['airline'].value_counts().reset_index()
airline_counts.columns = ['airline', 'count']

# Create a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='airline', y='count', hue='airline', palette='pastel', legend=False, data=airline_counts)
plt.title('Tweet Counts by Airlines')
plt.xlabel('Airline')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(plt)

