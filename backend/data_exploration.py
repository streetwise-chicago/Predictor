

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
crashes = pd.read_csv('~/repos/Predictor/backend/crash.csv')
crimes = pd.read_csv('~/repos/Predictor/backend/crime.csv')

# Count the frequency of each crash hour
crash_hour_counts = crashes['CRASH_HOUR'].value_counts()

# Sort by the index (crash hour) for a more meaningful chart
crash_hour_counts = crash_hour_counts.sort_index()

# Create the bar chart
plt.figure(figsize=(10,6))
plt.bar(crash_hour_counts.index, crash_hour_counts.values, color='b')
plt.xlabel('Crash Hour')
plt.ylabel('Frequency')
plt.title('Frequency of Crashes by Hour')
plt.show()

# Count the frequency of each crime hour
crime_hour_counts = crimes['crime_hour'].value_counts()

# Sort by the index (crime hour) for a more meaningful chart
crime_hour_counts = crime_hour_counts.sort_index()

# Create a bar chart
plt.figure(figsize=(10,6))
plt.bar(crime_hour_counts.index, crime_hour_counts.values, color='b')
plt.xlabel('Crime Hour')
plt.ylabel('Frequency')
plt.title('Frequency of Crimes by Hour')
plt.show()

# Create a scatter plot for each
plt.figure(figsize=(10,6))
plt.scatter(crashes['LONGITUDE'], crashes['LATITUDE'], alpha=0.5)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Scatter plot of crashes')
plt.show()

