'''
Kyle A. Destura BSCS 4A
3. Create a code that checks whether an integer is a Prime Number or not and 
display the first 25 10-digit Prime numbers
'''
import sys

#Algorithm is from https://en.wikipedia.org/wiki/Primality_test

def is_prime(number):
    if number <= 3:
        return number > 1
    
    if not number % 2 or not number % 3:
        return False
    
    i = 5
    stop = int(number**0.5)
    while i <= stop:
        if not number%i or not number%(i + 2):
            return False
        i += 6
    return True

def prime_numbers(max_number = 1000, max_count = 25):
    '''prime_numbers takes the prime numbers from a range 0 to  to Python max size integer
    
    param {max_number} starting number of a range 
    param {max_count} number of prime numbers to be stored
    returns list of prime numbers
    '''
    if max_number < 2 or max_count < 1:
        return "Check Parameters. {start} must be greater than 2 and {maxCount} must be greater than 1"
    else:
        digit_counter = 0
        my_list = list()
        for i in range(max_number, sys.maxsize):
            if is_prime(i):
                my_list.append(i)
                digit_counter += 1
                
            if digit_counter >= max_count:
                break
            
        return my_list

my_list = prime_numbers(10000000000)
print(my_list)
