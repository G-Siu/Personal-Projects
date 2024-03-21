import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('cheques-wines.csv')

# Display the first 5 rows
print(df.head())

# Print the column names and their data types
print(df.info())

# Grouping the data by 'Emisor' to find the total amount for each issuer
grouped_data = df.groupby('Emisor')['Monto'].sum().reset_index()

# Sort the data for better visualization
grouped_data_sorted = grouped_data.sort_values(by='Monto', ascending=False)

# Plotting the data
plt.figure(figsize=(12, 8))
sns.barplot(x='Monto', y='Emisor', data=grouped_data_sorted, hue='Emisor', palette="viridis", legend=False)
plt.title('Total Amount by Issuer')
plt.xlabel('Total Amount')
plt.ylabel('Issuer')
plt.show()
