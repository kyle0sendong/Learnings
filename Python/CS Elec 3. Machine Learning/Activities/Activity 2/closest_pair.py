"""
Kyle A. Destura BSCS 4A
5. Create a code that creates a list of 20 random integers between 1 and 1000. 
Display the closest pair among the list. The closest pair is a pair of two 
integers with the smallest difference. In the case of multiple existences of 
closest pair, display the smallest pair.
"""
import random
import sys


# Another simple solution is to copy the list, sort it then take the front-most pair
def get_difference(x, y):
    difference = 0
    if x > y:
        difference = x - y
    elif y > x:
        difference = y - x
    return difference


def is_smaller_pair(x1, y1, x2, y2):
    """ isSmallerPair evaluates which of 2 pair of integer is smaller
    
    {x1, y1} first pair of integers
    {x2, y2} second pair of integers
    returns the evaluation of which pair has smaller sum therefore it is smaller pair
    """
    return (x1 + y1) <= (x2 + y2)


def closest_pair(my_list):
    """closestPair, bruteforce method in retrieving the closest and smallest pair
    
    {myList} list of integers that will be evaluated
    returns a list of 2 index where the smallest and closest pair is found from the list.
    """

    my_list_length = len(my_list)
    my_list.append(0)
    my_list.append(99999999)

    pair_index = [my_list_length - 1, my_list_length - 2]  # Initial Closest Pair
    smallest_difference = sys.maxsize  # Initial Smallest Difference

    iterator = 0
    for i in range(my_list_length - 2):
        iterator += 1
        for j in range(iterator, my_list_length - 2):

            x1, y1 = my_list[i], my_list[j]
            x2, y2 = my_list[pair_index[0]], my_list[pair_index[1]]

            pair_difference = get_difference(x1, y1)
            smaller_pair = is_smaller_pair(x1, y1, x2, y2)

            if pair_difference < smallest_difference:
                smallest_difference = pair_difference

            if pair_difference == smallest_difference and smaller_pair:     # equal difference but smaller pair
                smallest_difference = pair_difference
                pair_difference[0], pair_index[1] = i, j

    # Remove the two added initial integer from list
    my_list.pop()
    my_list.pop()
    return pair_index


random_integer_list = list()

for i in range(20):
    randomInteger = random.randrange(1, 1000)
    random_integer_list.append(randomInteger)

pair = closest_pair(random_integer_list)
pair_value_1, pair_value_2 = random_integer_list[pair[0]], random_integer_list[pair[1]]
print("List of Integers:")
print(random_integer_list)
print("Closest and Smallest Pair: " + str(pair_value_1) + " and " + str(pair_value_2))
print("Difference: " + str(get_difference(pair_value_1, pair_value_2)))
print("Found in index: " + str(pair))
