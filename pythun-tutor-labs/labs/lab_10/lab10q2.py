import numpy as np
import matplotlib.pyplot as plt

# Load city names and continents
city_names = np.loadtxt('city_names.txt', dtype=str, delimiter=',')

# Load city data
data = np.loadtxt('city_data.txt', delimiter=',')

# Boolean indexing: cities with air quality index < 50 (4th column, index 3)
clean_air_mask = data[:, 3] < 50
clean_air_cities = data[clean_air_mask]

# Boolean indexing: European cities
europe_mask = city_names[:, 1] == 'Europe'
europe_data = data[europe_mask]
europe_names = city_names[europe_mask, 0]

# Create 2x2 subplot figure
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Top-left: Population density vs Cost of living
ax1 = axes[0, 0]
population_density = data[:, 6]
cost_of_living = data[:, 9]
ax1.scatter(population_density, cost_of_living, alpha=0.6, s=50)
ax1.set_xlabel('Population Density')
ax1.set_ylabel('Cost of Living Index')
ax1.set_title('Population Density vs Cost of Living')
ax1.grid(True, alpha=0.3)

# Top-right: Bar chart comparing average crime index
ax2 = axes[0, 1]
avg_crime_clean = np.mean(clean_air_cities[:, 5])
avg_crime_all = np.mean(data[:, 5])
ax2.bar(['Clean Air Cities', 'All Cities'], [avg_crime_clean, avg_crime_all], 
        color=['green', 'red'])
ax2.set_ylabel('Average Crime Index')
ax2.set_title('Crime Index Comparison')
ax2.grid(True, alpha=0.3, axis='y')

# Bottom-left: Pie chart of public transport usage in European cities
ax3 = axes[1, 0]
male_transport = np.sum(europe_data[:, 7])
female_transport = np.sum(europe_data[:, 8])
ax3.pie([male_transport, female_transport], 
        labels=['Male', 'Female'],
        autopct='%1.1f%%',
        startangle=90)
ax3.set_title('Public Transport Usage (Europe)')

# Bottom-right: Histogram of monthly average salary
ax4 = axes[1, 1]
monthly_salary = data[:, 4]
ax4.hist(monthly_salary, bins=5, color='purple', alpha=0.7, edgecolor='black')
ax4.set_xlabel('Monthly Average Salary')
ax4.set_ylabel('Number of Cities')
ax4.set_title('Salary Distribution')
ax4.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('question2_subplots.png', dpi=300, bbox_inches='tight')
plt.show()

# Create separate bar chart for European cities' cost of living
plt.figure(figsize=(10, 6))
europe_cost_of_living = europe_data[:, 9]
plt.bar(europe_names, europe_cost_of_living, color='skyblue')
plt.xlabel('City')
plt.ylabel('Cost of Living Index')
plt.title('Cost of Living in European Cities')
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('question2_europe_cost.png', dpi=300, bbox_inches='tight')
plt.show()