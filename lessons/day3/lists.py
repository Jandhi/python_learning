# The most straightforward container when you want to lots of something is a list
# In other languages, this might be known as an array or vector

my_numbers = [1, 2, 3, 4]

# a list can have multiple types
my_wallet = ["keys", 234, False]

# FOR LOOP
# when you want to do something FOR multiple things


for num in my_numbers:
    # I can do something to the thing I have in my wallet
    print(num)


# INDEXING
# When you want to "get" something from a list, we use the indexing operator
# Basically we use square brackets at the end of a list with an index
# Index 0 is the first index, so list[0] is the first item in the list

# WE START INDEXING AT 0
# FUCK YOU THAT'S WHY

print(my_numbers[0]) # prints the first item in the list
print(my_numbers[1]) # prints the second item ...
print(my_numbers[2]) # ........... third ...

# THINGS WE CAN DO WITH LISTS
print('--- THINGS WE CAN DO WITH LISTS ---')

# append to a list (aka add an item)
my_numbers.append(17)
print(my_numbers)

# remove first time an item appears from in a list
my_numbers.remove(17)
print(my_numbers)

# remove item at a specified index
item = my_numbers[1] # get the second item
my_numbers.remove(item) # remove the first time the second item appears
print(my_numbers)

# another way to do this
# pop just removes the item at index X
# in this case, index 1 is the SECOND item
# because programmers cannot count
my_numbers.pop(1)
print(my_numbers)

