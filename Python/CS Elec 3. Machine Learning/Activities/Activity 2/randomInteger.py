# =============================================================================
# Kyle A. Destura BSCS 4A
# 4. Create a code that creates a list of 100 random integers between 100 and 
# 100,000. Display the minimum and the maximum value among the randomly created
# list. Display also the list on the screen.
# =============================================================================

import random

myRandomInteger = list()

for i in range(100):
    myRandomInteger.append(random.randrange(100, 100000))

minimumValue = min(myRandomInteger)
maximumValue = max(myRandomInteger)
print("Minimum Value: " + str(minimumValue))
print("Maximum Value: " + str(maximumValue))
print("Random Integer List:")
print(myRandomInteger)