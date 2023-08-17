import pandas as pd

input_filename = 'crimes_adjusted.csv'
output_filename = 'clean_crimes.csv'
columns_to_remove = [0]  # List of column indices to be removed

# Read the CSV file into a DataFrame
data = pd.read_csv(input_filename)

# Drop the specified columns
data = data.drop(data.columns[columns_to_remove], axis=1)

# Write the modified data back to a new CSV file
data.to_csv(output_filename, index=False)

print("hello")

