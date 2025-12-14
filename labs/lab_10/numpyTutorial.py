from matplotlib import pyplot as plt
import numpy as np

# a = np.zeros(3)
# print(type(a)) # type is a class. prints an array of floats.

weather_data = np.loadtxt("weather_data.txt", delimiter = ",")
#print(weather_data[:, 1]) #  her satırın 2. değeri oldu.
temperature = weather_data[:, 1] # will be x axis.
humidity = weather_data[:, 2] # will be y axis.

coefficients = np.polyfit(temperature, humidity, 1)
polynomial = np.poly1d(coefficients)
# print(coefficients) # eğimini bulduk ve kesim noktasını bulduk. 1. dereceden bir doğru bu.
# print(polynomial) #  3.422 x + 1.872
# print(polynomial(20)) # x = 20 için değer kaç?

fitted_humidity = polynomial(temperature) # has a loop itself - the methdod actually.

plt.figure(figsize=(10, 6)) # 10x6
plt.scatter(temperature, humidity, color='red', label='Data Points', s=50)
# döngü yapıyor. [0] için temperature ve humidity ne? o noktaya kırmızı koy. 50 büyüklük. # gerçek veriler.

plt.plot(temperature, fitted_humidity, color='blue', linestyle='--', label='Fitted Line') # tahmin
# döngü var. [0] için sıcaklık ve o nemdeki hava durumu nedir?
# plt.xticks([15, 17, 19, 21, 23, 25]) 
# plt.xlim(15, 26) 

plt.xlabel('Average Temperature (°C)')
plt.ylabel('Average Humidity (%)')
plt.title('Average Humidity vs. Average Temperature')

# plt.savefig('question1_output.png', dpi=300, bbox_inches='tight')
plt.tight_layout()
plt.show()
print(f"Linear fit equation: y = {coefficients[0]:.2f}x + {coefficients[1]:.2f}")