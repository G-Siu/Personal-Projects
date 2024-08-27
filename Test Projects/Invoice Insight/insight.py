import pandas as pd

df = pd.read_csv("Invoices Dic - Facturas.tsv", sep="\t")
# Convert `Total Amount` to numeric after removing ','
df['Total Amount'] = (
    df['Total Amount'].astype(str).str.replace('[,]', '', regex = True).astype(float)
)

# Replace missing `Total Amount` values with the median
df['Total Amount'] = df['Total Amount'].fillna(df['Total Amount'].median())

# Group by `Sales Team` and calculate the median `Total Amount`
df_summ = df.groupby('Sales Team')['Total Amount'].median().reset_index()

# Sort the DataFrame
df_sorted = df_summ.sort_values(by='Total Amount')

# Print the DataFrame
print(df_sorted)

# Calculate the median of the entire `Total Amount` column
overall_median = df_sorted['Total Amount'].median()

# Calculate the absolute deviation from the overall median for each row
df_sorted['Absolute Deviation'] = abs(df_sorted['Total Amount'] - overall_median)

# Calculate the median of the Absolute Deviation column
MAD = df_sorted['Absolute Deviation'].median()

# Print the MAD value
print(f'The median absolute deviation (MAD) is: {MAD}')

import matplotlib.pyplot as plt

# Extract total amounts per sales team into separate lists
team1_amounts = df[df['Sales Team'] == 'Salesman 1']['Total Amount'].tolist()
team2_amounts = df[df['Sales Team'] == 'Salesman 2']['Total Amount'].tolist()
office_amounts = df[df['Sales Team'] == 'Office']['Total Amount'].tolist()
gov_amounts = df[df['Sales Team'] == 'Goverment']['Total Amount'].tolist()

# Create figure and axes
fig, ax = plt.subplots()

# Create boxplot with median markers
ax.boxplot([team1_amounts, team2_amounts, office_amounts, gov_amounts], labels=['Salesman 1', 'Salesman 2', 'Office', 'Goverment'], medianprops={'markerfacecolor': 'red'})

# Add overall median line
ax.axhline(overall_median, color='green', linestyle='--', label='Overall Median')

# Add MAD range as shaded area (approximate)
mad_upper = overall_median + MAD
mad_lower = overall_median - MAD
ax.fill_between([0, 3.5], mad_upper, mad_lower, color='lightblue', alpha=0.5, label='MAD Range')

# Customize plot appearance and labels
ax.set_xlabel('Sales Team')
ax.set_ylabel('Total Amount')
ax.set_title('Distribution of Total Amounts and MAD')
ax.legend()

# Show the plot
plt.show()


# Consistency constant to calculate outlier from MAD
def outlier_cutoff(amounts):
    return sum(abs(x - overall_median) > 1.4826 * MAD for x in amounts)


# Get outlier count per sales team
outlier_counts = df.grouby("Sales Team")["Total Amount"].agg(outlier_cutoff)

# Calculate percentages
outlier_percentages = (outlier_counts / df["Sales Team"].value_counts()) * 100

# Get the sales team with the highest percentage of outliers
highest_outlier_team = outlier_percentages.idxmax()
highest_outlier_percentage = outlier_percentages.max()

print(outlier_percentages)
print(highest_outlier_team, highest_outlier_percentage)