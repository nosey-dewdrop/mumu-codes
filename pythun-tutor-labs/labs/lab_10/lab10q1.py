import numpy as np
import matplotlib.pyplot as plt

# Load weather data
weather_data = np.loadtxt('weather_data.txt', delimiter=',')

# Extract temperature (2nd column, index 1) and humidity (3rd column, index 2)
temperature = weather_data[:, 1]
humidity = weather_data[:, 2]

# Find the first-degree polynomial (linear fit)
coefficients = np.polyfit(temperature, humidity, 1)
polynomial = np.poly1d(coefficients)

# Generate fitted line values
fitted_humidity = polynomial(temperature)

# Create the plot
plt.figure(figsize=(10, 6))
plt.scatter(temperature, humidity, color='red', label='Data Points', s=50)
plt.plot(temperature, fitted_humidity, color='blue', linestyle='--', label='Fitted Line')

plt.xlabel('Average Temperature (°C)')
plt.ylabel('Average Humidity (%)')
plt.title('Average Humidity vs. Average Temperature')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('question1_output.png', dpi=300, bbox_inches='tight')
plt.show()

print(f"Linear fit equation: y = {coefficients[0]:.2f}x + {coefficients[1]:.2f}")