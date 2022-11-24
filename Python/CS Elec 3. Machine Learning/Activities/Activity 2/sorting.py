'''
Kyle A. Destura BSCS 4A
1. Create a code that will ask the user to input 25 integers and sort these 
numbers in an ascending order without using the built-in SORT Function of 
Python. Consider using the easiest Sorting # Algorithm (Bubble Sort) for this
Activity. Display the sorted list after the process. Display also the result 
in a Descending Order.
'''
def bubble_sort(my_list):
    list_length = len(my_list)
    swapped = False

    for i in range(list_length - 1):
        for j in range(0, list_length-i-1):

            if my_list[j] > my_list[j + 1]:
                swapped = True
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

        if not swapped:
            return

print("Input 25 integers.")
int_list = list()
iterator = 1

while iterator < 26:
    try:
        input_int = int(input(str(iterator) + ": "))
        int_list.append(input_int)
        iterator += 1
    except ValueError:
        print("Input integer only.") 
        continue

bubble_sort(int_list)

print("Sorted List: ")
for i in int_list:
    print(i, end = " ")

print("\nReverse Sorted List: ")
for i in reversed(int_list):
    print(i, end = " ")
 