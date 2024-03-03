import numpy as np
import matplotlib.pyplot as plt

# Simulated air quality data (replace this with your actual data)
cities = ['Delhi', 'Mumbai', 'Chennai', 'Kolkata']
pollutants = ['PM2.5', 'PM10', 'NO2', 'SO2']

# Simulate random air quality data for each city and pollutant
data = np.random.rand(len(cities), len(pollutants)) * 100

# Display the simulated data
print("Simulated Air Quality Data:")
print("Cities:", cities)
print("Pollutants:", pollutants)
print("Air Quality Data:\n", data)

# Calculate mean and standard deviation for each pollutant
mean_values = np.mean(data, axis=0)
std_dev_values = np.std(data, axis=0)

# Plotting bar charts for mean and standard deviation
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

ax[0].bar(pollutants, mean_values, color='blue', alpha=0.7, label='Mean')
ax[0].set_ylabel('Mean Value')
ax[0].set_title('Mean Air Quality Values for Each Pollutant')

ax[1].bar(pollutants, std_dev_values, color='orange', alpha=0.7, label='Standard Deviation')
ax[1].set_ylabel('Standard Deviation')
ax[1].set_title('Standard Deviation of Air Quality Values for Each Pollutant')

plt.tight_layout()
plt.show()
