# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 15:03:35 2023

@author: Damea
"""
##Basic Subscriber VS. Not Subscriber totals and Plot
import pandas as pd
import matplotlib.pyplot as plt

file_path = "Chart data.csv"
subscriber_dataframe = pd.read_csv(file_path)
grouped_subscriber_df = subscriber_dataframe.groupby('Subscription status')['Views'].sum().reset_index()

colors = ['purple', 'red']

plt.bar(grouped_subscriber_df['Subscription status'], grouped_subscriber_df['Views'], color = colors)

plt.xlabel('Subscription Status')
plt.ylabel('Total Views')
plt.title('Not Subscribed Vs. Subscribed Views (11/10/2023 - 12/7/2023)')

for index, value in enumerate(grouped_subscriber_df['Views']):
    plt.text(index, value +1, str(value), ha='center', va='bottom')
    
plt.show()

# Not Subscriber Vs. Subscriber Watch Time

file_path1 = 'Table data.csv'

subscriber_dataframe1 = pd.read_csv(file_path1)

filtered_subscriberdf1 = subscriber_dataframe1[subscriber_dataframe1['Subscription status'] != 'Total']

grouped_subscriber_df1 = filtered_subscriberdf1.groupby('Subscription status')['Watch time (hours)'].sum().reset_index()

plt.figure(figsize = (8, 8))

plt.pie(grouped_subscriber_df1['Watch time (hours)'], labels=grouped_subscriber_df1['Subscription status'], autopct='%1.1f%%', colors=['lightblue', 'lightgreen'], startangle=90)


plt.gca().set_aspect('equal')
plt.text(0, 0, f"Total\n{subscriber_dataframe1['Watch time (hours)'].sum()} hours", ha='center', va='center', fontsize=12, color='black')

plt.xlabel('Subscription Status')
plt.ylabel('Total Watch Time (Hours)')
plt.title('Not Subscribed Vs. Subscribed Watch Time (11/10/2023 - 12/7/2023)')

plt.show()
colors1 = ['black', 'orange']

plt.bar(grouped_subscriber_df1['Subscription status'], filtered_subscriberdf1['Watch time (hours)'], color=colors1)

plt.xlabel('Subscription Status')
plt.ylabel('Watch Time in Hours')
plt.title('Watch Time for Subscribers Vs. Not Subscribers (11/10/2023 - 12/7/2023)')

for index, value in enumerate(grouped_subscriber_df1['Watch time (hours)']):
    plt.text(index, value +1, str(value), ha='center', va='bottom')

plt.show()

# Views on Dates to get average views per day of the week

file_path2 = 'Totals.csv'

view_datedf = pd.read_csv(file_path2)

Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

count = 4
view_datedf['Date'] = pd.Categorical(view_datedf['Date'], categories = Days)
for i in range(len(view_datedf['Date'])):
    view_datedf.loc[i, 'Date'] = Days[count]
    count = (count + 1) % 7  # Increment count, reset to 0 after reaching 6

daysdf = view_datedf.groupby('Date')['Views'].sum().reset_index()
colors = ['blue', 'red', 'black', 'purple', 'yellow', 'green', 'orange']


plt.bar(daysdf['Date'], daysdf['Views'], color=colors)
plt.xlabel('Days of the week')
plt.ylabel('Average Views')
plt.title('Average Views For Days of The Week (11/10/2023 - 12/7/2023)')
print(daysdf)


