# Let's first read the uploaded CSV file to understand its structure and find out the data related to 'Azucar'
import pandas as pd

# Load the CSV file
df = pd.read_csv('trapiche_ingenio_nv.csv')

# Display the first few rows of the dataframe to understand its structure
df.head()

# Sum up the 'Azucar' for each date and find the date with the highest total 'Azucar'
total_azucar_per_date = df.groupby('Fecha')['Azucar'].sum().reset_index()

# Find the date with the maximum total 'Azucar'
most_productive_date = total_azucar_per_date.loc[total_azucar_per_date['Azucar'].idxmax()]

print(most_productive_date)
