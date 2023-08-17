import pandas as pd

# Read the CSV file into a DataFrame
csv_file_path = 'crashes.csv'
data = pd.read_csv(csv_file_path)

# Identify rows to remove based on a specific condition (for example, removing rows where a column value is below a threshold)
condition = data["L"].isnull()

# Filter out the rows that meet the condition
data_filtered = data[~condition]

# Write the modified data back to the CSV file
new_csv_file_path = 'modified_file.csv'
data_filtered.to_csv(new_csv_file_path, index=False)

print("hello")
