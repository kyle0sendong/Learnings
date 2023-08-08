"""
Kyle A. Destura BSCS 4A
4. Create a code that creates a list of 100 random integers between 100 and 
100,000. Display the minimum and the maximum value among the randomly created
list. Display also the list on the screen.
"""
import random

random_integer = list()

for i in range(100):
    random_integer.append(random.randrange(100, 100000))

minimum_value = min(random_integer)
maximum_value = max(random_integer)
print("Minimum Value: " + str(minimum_value))
print("Maximum Value: " + str(maximum_value))
print("Random Integer List:")
print(random_integer)
