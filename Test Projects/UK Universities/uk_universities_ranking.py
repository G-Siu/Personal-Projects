import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('uk_universities.csv')

# Display the first 5 rows
print(df.head())

# Get information about the columns
print(df.info())

# Remove the '%' from the 'International_students' and 'Student_satisfaction' columns
df['International_students'] = pd.to_numeric(
    df['International_students'].str.rstrip('%')
).fillna(0)
df['Student_satisfaction'] = pd.to_numeric(
    df['Student_satisfaction'].str.rstrip('%')
).fillna(0)

# Group by 'Region' and calculate the mean of 'UK_rank' and 'World_rank'
average_rank_df = df.groupby('Region')[['UK_rank', 'World_rank']].mean()

# Print the average_rank_df DataFrame
print(average_rank_df)
