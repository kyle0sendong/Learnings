# =============================================================================
# Kyle A. Destura BSCS 4A
# 3. Create a code that checks whether an integer is a Prime Number or not and 
# display the first 25 10-digit Prime numbers
# =============================================================================

import sys

#Algorithm is from https://en.wikipedia.org/wiki/Primality_test

def isPrime(number):
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


# primeNumbers. Takes the prime numbers from a range to Python max size integer
# @param {start} starting number of a range 
# @param {maxCount} number of prime numbers to be stored
# @returns list of prime numbers
# @throws parameter checking
def primeNumbers(start = 1000000000, maxCount = 25):
    
    if start < 2 or maxCount < 1:
        return "Check Parameters. {start} must be greater than 2 and {maxCount} must be greater than 1"
    else:
        digitCounter = 0
        myList = list()
        for i in range(start, sys.maxsize):
            if isPrime(i):
                myList.append(i)
                digitCounter += 1
                
            if digitCounter >= maxCount:
                break
            
        return myList

myList = primeNumbers(1000000000000000)
print(myList)


# =============================================================================
# isPrime. evaulates if a number is a prime number or not
# @param {number} number to be evaluated
# @returns a boolean if a number is boolean or not
# @throws parameter checking
#def isPrime(number):
#      if number < 2:
#          return "Check Parameters. {number} must be greater than 2."
#      else:
#          isPrime = True
#          for i in range(2, int(number/2)):
#              if number % i == 0:
#                  isPrime = False
#          return isPrime
# 
# =============================================================================