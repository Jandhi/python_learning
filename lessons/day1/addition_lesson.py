# Let's add some numbers
print('1' + '1') # prints 11 because '1' is the string character one, NOT a number
print(1 + 1) # prints 2 becuse 1 is the actual number


# To convert a string to an integer, we can use int()

my_grade = int('170')
my_grade = my_grade + 5
print(my_grade)

# We assign number to be equal to the console input
number = input()
# VARIABLE <- VALUE

# The following would give an error, because *number* is not recognized as an integer, but is a STRING
# print(number + 1)

# This step is where we set "number" to BE an integer, which will make sure it is not a string
# Specifically it is the "integer form of that string"
number = int(number)
print(number + 1)


