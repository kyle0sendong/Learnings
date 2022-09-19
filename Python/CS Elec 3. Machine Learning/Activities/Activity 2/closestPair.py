# =============================================================================
# 5. Create a code that creates a list of 20 random integers between 1 and 1000. 
# Display the closest pair among the list. The closest pair is a pair of two 
# integers with the smallest difference. In the case of multiple existences of 
# closest pair, display the smallest pair.
# =============================================================================

# I have encountered this problem in an activity before, I used to sort the list then take the
# smallest pair. Going back to this problem, the downside is that list will be changed.
# Also the index of the closest and smallest pair cannot be retrieved.
 
import random
import sys

# getDifference takes the difference of 2 integers
# @param {x, y} integers to be subtracted
# @returns the difference of the {x, y}
def getDifference(x, y):
    difference = 0
    if x > y:
        difference = x - y
    elif y > x:
        difference = y - x
    return difference

# isSmallerPair evaluates which of 2 pair of integer is smaller
# @param {x1, y1} first pair of integers
# @param {x2, y2} second pair of integers
# @returns the evaluation of which pair has smaller sum therefore it is smaller pair
def isSmallerPair(x1, y1, x2, y2):
    return (x1 + y1) <= (x2 + y2)

# closestPair, bruteforce method in retrieving the closest and smallest pair
# @param {myList} list of integers that will be evaluated
# @returns a list of 2 index where the smallest and closest pair is found from the list.
def closestPair(myList):
    
    myListLength = len(myList)
    myList.append(0) 
    myList.append(99999999)
    
    pairIndex = [myListLength-1, myListLength-2] #Initial Closest Pair
    smallestDifference = sys.maxsize #Initial Smallest Difference
    
    iterator = 0
    for i in range(myListLength-2):
        iterator += 1
        for j in range(iterator, myListLength-2):
            
            x1, y1 = myList[i], myList[j]
            x2, y2 = myList[pairIndex[0]], myList[pairIndex[1]]
        
            pairDifference = getDifference(x1, y1)
            smallerPair = isSmallerPair(x1, y1, x2, y2)
            
            if pairDifference < smallestDifference:
                smallestDifference = pairDifference
                
            if pairDifference == smallestDifference and smallerPair:
                smallestDifference = pairDifference
                pairIndex[0], pairIndex[1] = i, j           
    
    myList.pop()  
    myList.pop() #Remove the two added initial integer from list
    return pairIndex

myRandomIntegerList = list()

for i in range(20):
    randomInteger = random.randrange(1, 1000)
    myRandomIntegerList.append(randomInteger)
    
pair = closestPair(myRandomIntegerList)
pairValue1, pairValue2  = myRandomIntegerList[pair[0]], myRandomIntegerList[pair[1]]
print("List of Integers:")
print(myRandomIntegerList)
print("Closest and Smallest Pair: " + str(pairValue1) + " and " + str(pairValue2))
print("Difference: " + str(getDifference(pairValue1, pairValue2)))
print("Found in index: " + str(pair))
   
# test = [1,3,2,2,0,0,9,9]
# print(test)
# print(closestPair(test)) #should return index 4, 5