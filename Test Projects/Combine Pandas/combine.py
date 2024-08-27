# import pandas as pd
#
# # Read the CSV file into a pandas dataframe
# df1 = pd.read_csv('sales.csv')
#
# # Read the JSON file into a pandas dataframe
# df2 = pd.read_json('students.json')
#
# # Combine the two dataframes using concatenation
# combined_df = pd.concat([df1, df2])
#
# # Print the combined dataframe
# print(combined_df)


import pandas as pd

# Load the CSV file
csv_data = pd.read_csv('sales.csv')

# Load the JSON file
json_data = pd.read_json('students.json')

# Combine the two datasets
combined_data = pd.concat([csv_data, json_data], ignore_index=True)

print(combined_data)