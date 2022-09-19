# =============================================================================
# Kyle A. Destura BSCS 4A
# 2. Using the situation above, create a similar code but using the built-in 
# SORT function of the Python Language.
# =============================================================================

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

myIntList.sort()

print("Sorted List: ")
for i in myIntList:
    print(i, end = " ")

print("\nReverse Sorted List: ")
for i in reversed(myIntList):
    print(i, end = " ")
    
    
    