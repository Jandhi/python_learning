


counter = 0 #we set a variable (counter) equal to 0
while True: #we establish a "while loop" which while true will do....
    print('a') # print a 
    counter = counter + 1 #we add 1 to the counter variable

    if counter == 3:
        break #if the counter hits 3, we "STOP THE STEAL" (we exit the while loop)

# this is an alternative, better approach
counter = 0
while counter < 3:
    print('b')
    counter += 1

# while loops can be used in place of for loops
my_list = [1, 2, 3, 4, 5]
#  indices 0  1  2  3  4 
#  length is 5
# NOTE: the length of a list is always one more than the index of the last item
# a way to iterate through that list, is to look at the item at each index

print(my_list)
print('IS DIFFERENT THAN')

# len() finds the length of a given list
index = 0
while index < len(my_list): # loop until the index N == length of list, at which point we have gone beyond the end of the list
    # in other words, for any list of length N, the index N will not exist in a list
    item = my_list[index]

    # do something with item
    print(item)

    index += 1

# this is the same as
for item in my_list:
    print(item)

# MY MEMORY

# counter: 0
# print a
# counter: 1
# we don't break
# the rest of the if loop gets skipped
# print a
# counter: 2
# if doesn't proc
# print a
# counter: 3
# AND NOW WE BREAK BABY