# import matplotlib

# print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

# Simulating daily temperature data
days = np.arange(1,20)
temperature = np.random.normal(loc=25, scale=5, size=len(days))

plt.plot(days, temperature, marker='o')
plt.title('Daily Temperatures in August')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

# months = np.arange(1,13)
# sales = np.random.randint(2000, 4000, size=len(months))
# plt.plot(months, sales, color='red', linestyle='--', marker='o')
# plt.title("Monthly Sales of Product ")
# plt.xlabel("Month")
# plt.ylabel("Sales (Units)")
# plt.grid(True)
# plt.show()