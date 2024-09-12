# LOGIC

# BOOLEANS
# to store the idea of TRUE or FALSE you use a boolean
False 
True

# those are the only two boolean numbers

# you can generate them using statements such as 

# EQUALITY
# ==

# Equality is checked using DOUBLE equals 
# Assignemnt is single equals

x = 3 # assignment
x = 4 # notice this doesn't compare 3 to 4, it just changes x to 4

print(x == 3) # true or false depending on what x is

print(4 * 4 == 2 ** 4)

# compare strings!
x = input()
print(x == 'test') # will only say true if we enter 'test' into the console

# COMPARISONS
# <  is less than
# >  is greater than
# <= is less than OR equal to
# >= is greater than or equal to

print(2 > 3) # clearly false
print(31 >= 5) 
# equivalent to
print(31 > 5 or 31 == 5)

# two logic operators you might already know
# AND and OR
# they are operators that take in BOOLs and output a BOOL
# they take in two truth values and output a truth value

# AND operator is true IF and ONLY IF x and y

# TRUTH TABLE FOR AND
# X     Y     | X and Y
# True  True  | True
# False True  | False
# True  False | False
# False False | False


# AND operator is true IF and ONLY IF either x or y is true

# TRUTH TABLE FOR OR
# X     Y     | X or Y
# True  True  | True
# False True  | True
# True  False | True
# False False | False

print(1 == 1 and 2 == 3)
print(1 == 1 or 2 == 3)

