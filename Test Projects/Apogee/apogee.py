import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("3.xlsx")

apogees = df["Apogee (km)"]

plt.hist(apogees, bins=100)
plt.xlabel("Apogee (km)")
plt.ylabel("Frequency")
plt.title("Satellite Apogees Histogram")
plt.show()
