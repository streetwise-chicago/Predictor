

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('/Users/grantharris/repos/Predictor/backend/clean_crash_data.csv')

# Count the frequency of each crash hour
crash_hour_counts = data['CRASH_HOUR'].value_counts()

# Sort by the index (crash hour) for a more meaningful chart
crash_hour_counts = crash_hour_counts.sort_index()

# Create the bar chart
plt.figure(figsize=(10,6))
plt.bar(crash_hour_counts.index, crash_hour_counts.values, color='b')
plt.xlabel('Crash Hour')
plt.ylabel('Frequency')
plt.title('Frequency of Crashes by Hour')
plt.show()