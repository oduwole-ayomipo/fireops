import random
import numpy as np
Generate = []
for i in range (0,3):
    n = random.randint(1, 100)
    Generate.append(n)

# converting the list to an array

Generate = np.array(Generate)
print(Generate)

# Assigning the individual array to a variable

Oxygen = Generate[0]
Temperature = Generate[1]
Humidity = Generate[2]

print("Oxygen:      ", Oxygen)
print("Temperature: ", Temperature)
print("Humidity:    ", Humidity)

