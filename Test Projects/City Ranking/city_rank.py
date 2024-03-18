# import pandas as pd
#
# # Read the CSV file into a DataFrame
# df = pd.read_csv('Cities with the Best Work-Life Balance 2022.csv')
#
# # Display the first 5 rows
# print(df.head().to_markdown(index=False, numalign="left", stralign="left"))
#
# # Print the column names and their data types
# print(df.info())

# # Remove '-' values in the `2021` column
# df = df[df['2021'] != '-']
#
# # Convert the `2021` column to numeric
# df['2021'] = pd.to_numeric(df['2021'])
#
# # Filter the data to only include rows where the value in the `2021` column is missing
# df_new_cities = df[df['2021'].isna()]
#
# # Count the number of rows in the filtered data
# num_new_cities = df_new_cities.shape[0]
#
# # Print the number of cities new to the 2022 list
# print(f"There are {num_new_cities} cities new to the 2022 list.")

import pandas as pd

# Load the data from the uploaded file
df_new = pd.read_csv('Cities with the Best Work-Life Balance 2022.csv')

# Check for cities with '-' in the 2021 column, indicating they are new to the list
new_cities_count = df_new[df_new['2021'] == '-'].shape[0]

print(new_cities_count)
