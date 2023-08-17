import pandas as pd

# Read the entire CSV file
input_file = 'clean_crime_data.csv'
df = pd.read_csv(input_file)

# Keep only the first 10,000 rows
df = df.head(10000)

# Write the first 10,000 rows to a new CSV file
output_file = 'crime.csv'
df.to_csv(output_file, index=False)

print("hello")
