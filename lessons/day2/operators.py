# OPERATORS

# you already know the most common operator, +
print(1 + 1)

# There are other common math operators
print(1 - 1)

print(- 9)

# Multiplication
# we can't use x because its a letter
print(2 * 3)

# division
# we use the backlash / 
print(11 / 3) 

# by default, dividing integers creates a FLOAT, or a number with a decimal
# AKA floating point number

# to round down to the nearest integer, we can use double backlash
# //
# ROUND DOWN means chop off the decimal, don't care what's there

print(11 // 3)

# equivalent to this
print(int(11 / 3)) # This is a more tedious way to do the same thing

# just a review for integer conversion
print('INTEGER CONVERSION')
print(int(3))
print(int('3'))
print(int(3.5))

# another useful operator: the modulo / modulus operator %
# gets you the remainder when doing whole number division

print(11 % 3) # prints 2

print('A USE CASE FOR MODULOS:')
# A USE CASE FOR MODULO
# check if a number is even
x = 10
print((x / 2) == (x // 2)) # Longer, less efficient method

print(x % 2 == 0) # Faster!

# exponential operator
2 ** 5 # this is 2 to the power of 5



