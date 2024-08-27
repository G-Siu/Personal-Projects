import json
import matplotlib.pyplot as plt

# Load JSON data
with open('objectOne.json', 'r') as file:
    data = json.load(file)

# Assuming your data structure looks like the one provided earlier

# Function to plot data
def plot_data(x_data, y_data, x_label, y_label, title):
    plt.figure()
    plt.plot(x_data, y_data, marker='o')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.show()

# Extracting data for different plots
thickness = [item['Polyethylene'] for item in data]
volumes = [item['Volume of PE'] for item in data]
masses = [item['Mass of PE'] for item in data if 'Mass of PE' in item]  # This
# assumes Mass_of_PE exists in all items

# Plot Volume of PE vs Thickness
plot_data(thickness, volumes, 'Thickness of Polyethylene (m)', 'Volume of PE (m^3)', 'Volume of Polyethylene vs Thickness')

# Plot Mass of PE vs Thickness
# Here we need to handle the formatting of mass (remove commas or convert to float)
masses_cleaned = [float(str(mass).replace(',', '')) if isinstance(mass, str) else mass for mass in masses]
plot_data(thickness[:len(masses_cleaned)], masses_cleaned, 'Thickness of Polyethylene (m)', 'Mass of PE (kg)', 'Mass of Polyethylene vs Thickness')

# If you want to show how height, length or width changes with thickness:
for dimension in ['Height', 'Length', 'Width']:
    dimensions = [item[dimension] for item in data]
    plot_data(thickness, dimensions, 'Thickness of Polyethylene (m)', f'{dimension} (m)', f'{dimension} vs Thickness')