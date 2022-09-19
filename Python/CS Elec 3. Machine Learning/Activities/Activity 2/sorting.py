# =============================================================================
# Kyle A. Destura BSCS 4A
# 1. Create a code that will ask the user to input 25 integers and sort these 
# numbers in an ascending order without using the built-in SORT Function of 
# Python. Consider using the easiest Sorting # Algorithm (Bubble Sort) for this
# Activity. Display the sorted list after the process. Display also the result 
# in a Descending Order.
# =============================================================================

def bubbleSort(myList):
    n = len(myList)
    swapped = False
    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            
            if myList[j] > myList[j + 1]:
                swapped = True
                myList[j], myList[j + 1] = myList[j + 1], myList[j]
                
        if not swapped:
            return

print("Input 25 integers.")
myIntList = list()
iterator = 1

while iterator < 26:
    try:
        inputInt = int(input(str(iterator) + ": "))
        myIntList.append(inputInt)
        iterator += 1
    except ValueError:
        print("Input integer only.") 
        continue
    
bubbleSort(myIntList)

print("Sorted List: ")
for i in myIntList:
    print(i, end = " ")

print("\nReverse Sorted List: ")
for i in reversed(myIntList):
    print(i, end = " ")
    
    
    