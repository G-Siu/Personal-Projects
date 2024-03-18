import pandas as pd

df = pd.read_csv('Monkey_Pox_Cases_Worldwide.csv')
print(df.head())
df.info()

total_confirmed_cases = df['Confirmed_Cases'].sum()
print(total_confirmed_cases)

country_with_most_cases = df['Confirmed_Cases'].idxmax()
print(country_with_most_cases)

total_hospitalized = df['Hospitalized'].sum()
hospitalization_rate = (total_hospitalized / total_confirmed_cases) * 1000
print(hospitalization_rate)

average_confirmed_cases = df['Confirmed_Cases'].mean()
print(average_confirmed_cases)