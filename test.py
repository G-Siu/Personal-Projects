import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('Wild_by_Aura_Final.xlsx')

# Split the Age column
df['Age_Group'] = pd.cut(df['Age'].str.split('-').str[0].astype(int), bins=[18, 25, 31, 41], labels=['18-24', '25-30', '31-40'])

# Group data by Age_Group and calculate average Transaction Amount
average_transaction_per_age = df.groupby('Age_Group')['Transaction Amount'].mean()

# Round to two decimal places
average_transaction_per_age = average_transaction_per_age.apply('{0:.2f}'.format)

# Create a new DataFrame
new_df = pd.DataFrame({'Age Group': average_transaction_per_age.index, 'Average Transaction Amount': average_transaction_per_age.values})

# Print the new DataFrame
print(new_df.to_markdown(index=False))