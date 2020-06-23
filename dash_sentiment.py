import sqlite3
import pandas as pd  

conn = sqlite3.connect('twitter.db')
c = conn.cursor()

df = pd.read_sql("SELECT * FROM sentiment WHERE tweet LIKE '%ethereum%' ORDER BY unix DESC LIMIT 1000", conn)
df.sort_values('unix', inplace=True)

#Smoothing out sentiment analysis
df['smoothed_sentiment'] = df['sentiment'].rolling(int(len(df)/5)).mean() #rolling avg using 20% of size of total data
df.dropna(inplace=True)

print(df.tail)


