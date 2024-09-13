from random import randint

# For every number in some unknown list of numbers

# First, write the number,
# then
# Write fizz if the number is divisible by 3
# Write buzz if the number is divisible by 5
# Write fizzbuzz if the number is divisible by both


# The RANGE operator includes 0, and excludes whatever top number you give it
# for example, range(2) yields 0 and 1

my_numbers = [randint(0, 100) for _ in range(randint(1, 100))] # My numbers is a list of numbers of mysterious length and contents
    
#if (number % 3 == 0 and not number % 5 == 0):
 #   print ('fizz') 

for num in my_numbers:
    
    print(num)

    # in this context, tabbed over once
    # we a variable called num, which stores the number in our current iteration
    
    if (num % 3 == 0):
        print('fizz')

    if (num % 5 == 0):
        print ('buzz')

    if (num % 5 == 0 and num % 3 == 0):
        print ('fizzbuzz')