# CALCULATOR APP
# We're gonna ask the user for two numbers
# And then we'll ask for an operation
# And then we perform that operation

# The catch: We want to ask the user for the correct input until they give
# something that matches what we expect

# we're gonna make a loop that ensures we get the right sort of input


my_input = input('Give me a number\n').strip()
# strip is a handy little function that removes all whitespace (ie spaces and shit)
# from the edges of a string
# this was " 25" will become "25"

my_input.isdigit() 

# the dot operator allows you to access things belonging to an object
# some functions belong to objects, meaning they operate on them
# these are known as methods
# the .isdigit() function tells you whether a string is a digit
# isdigit() is method belonging to strings, and only strings

# the first problem:
# I want an input where isdigit() resolves to true
# AKA if isdigit is NOT true, I want you to loop, and ask for it again

while not my_input.isdigit():
    print(f'Error: {my_input} is NOT a number') # this is an fstring

    # aka format string
    # if you put f right in front of a string, it means you can drop in variables
    # and other values into the string to be a part of it
    # more economical and useful than just using + for strings

    my_input = input('Give me a number\n').strip()

# because it will continuously loop when there's incorrect answers
# we can assume at this point that the answer is CORRECT, ie it is a digit
# no additional ifs needed

int_variable_1 = (int(my_input))

# technically, we can reuse the my_input variable to store the new input
# since we already saved the integer version in int_variable_1
my_input2 = input('Give me a number\n').strip()

while not my_input2.isdigit():
    print(f'Error: {my_input2} is NOT a number')

    my_input2 = input('Give me a number\n').strip()

int_variable_2 = (int(my_input2))


# so we've asked the user for one number
# I want you to save that as an integer variable, and then do the same thing again, and save it as another integer variable

# THEN I want you to make the user enter either +, -, *, or /
# loop if they give something that ISN'T that
operations = ['+', '-', '*', '/']
my_input3 =  input('Provide operation\n').strip()

while my_input3 not in operations:
    print(f'Error: {my_input3} is NOT an operation')

    my_input3 = input('Provide operation\n').strip()

# HINT: the in operator checks whether an item appears in a list
# e.g.
if 3 in [1, 2, 3]:
    pass # this happens only if 3 is in the list

# finally, perform the operation given between the two numbers given and print to output
# (you can use if to check against each symbol)

if my_input3 == '+':
    print(int_variable_1 + int_variable_2)

if my_input3 == '-':
    print(int_variable_1 - int_variable_2)

if my_input3 == '*':
    print(int_variable_1 * int_variable_2)

if my_input3 == '/':
    print(int_variable_1 / int_variable_2)