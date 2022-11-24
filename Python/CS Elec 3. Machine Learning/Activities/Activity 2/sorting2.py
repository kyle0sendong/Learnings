'''
Kyle A. Destura BSCS 4A
2. Using the situation above, create a similar code but using the built-in 
SORT function of the Python Language.
'''
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

int_list.sort()

print("Sorted List: ")
for i in int_list:
    print(i, end = " ")

print("\nReverse Sorted List: ")
for i in reversed(int_list):
    print(i, end = " ")
