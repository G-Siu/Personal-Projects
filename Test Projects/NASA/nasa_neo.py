import pandas as pd

df = pd.read_csv('nasa_neo_v2.csv')
# print(df.head())
# df.info()

# Filter the dataframe for 'orbiting_body' Earth
earth_df = df[df['orbiting_body'] == 'Earth']

# Calculate the average 'est_diameter_max' and 'relative_velocity' for 'orbiting_body' Earth
avg_est_diameter_max = earth_df['est_diameter_max'].mean()
avg_relative_velocity = earth_df['relative_velocity'].mean()

# Find the asteroid with minimum 'miss_distance' for Earth and is hazardous
min_miss_distance_hazardous_df = earth_df[earth_df['hazardous'] == True].nsmallest(1, 'miss_distance')

# Calculate its average 'est_diameter'
avg_est_diameter_hazardous = min_miss_distance_hazardous_df[['est_diameter_min', 'est_diameter_max']].mean(axis=1).mean()

# Find the asteroid(s) that are in the middle if we order them by 'miss_distance' and their hazardous is false
non_hazardous_df = earth_df[earth_df['hazardous'] == False].sort_values(by='miss_distance')
middle_index = non_hazardous_df.shape[0] // 2
if non_hazardous_df.shape[0] % 2 == 0:
    middle_asteroids_df = non_hazardous_df.iloc[[middle_index - 1, middle_index]]
else:
    middle_asteroids_df = non_hazardous_df.iloc[[middle_index]]

# Calculate its average 'est_diameter'
avg_est_diameter_middle_non_hazardous = middle_asteroids_df[['est_diameter_min', 'est_diameter_max']].mean(axis=1).mean()

print(avg_est_diameter_max, avg_relative_velocity, avg_est_diameter_hazardous,
 avg_est_diameter_middle_non_hazardous)