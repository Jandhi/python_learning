#Assignment 4 
#Have the user enter a number
#That number will be the size of a list of numbers they want to sum up

#Then have them enter N numbers, where N is the number they entered in the beginning
#Put these numbers into a list 

#Finally, calculate the sum of the numbers in that list, and print it to console

#I want you to have error check loops for every numerical input.  
#This means you'll be using while loops in every part of this problem...
#and might even need to create a while loop inside of a while loop

# EXAMPLE INPUT 1

# Enter the length of your list
# 2
# Enter a number
# 1
# Enter a number
# 2
# Your sum is 3


# Enter the length of your list
# 4
# Enter a number
# 6
# Enter a number
# 6
# Enter a number
# 6
# Enter a number
# 5
# Your sum is 23

#----Step 1----
#We need to have the user enter a number
my_input = input("Enter the number that will be the size of a list of numbers you want to sum.\n").strip()
#prompt = int(input("Enter the number that will be the size of a list of numbers you want to sum."))

#now we need to create an empty list
my_list = []

#I assume that we need to do the following:
while not my_input.isdigit():
    print(f'Error: {my_input} is NOT a number')
    my_input = input("Please enter a valid integer for the list size:\n").strip()

#The above script was pulled from our last lesson, but essentially I made it ask me for a number...
#Then when I gave a non-number response it would ask me to provide a valid integer

#---Step 4---
#I think now we need to convert the number input in the console into being the size of the list

list_size = int(my_input)

#This is me making a variable for the list size that will equal an integer of the input
#I do think this is wrong though


#Spent an ungodly amount of time researching what the counter properly does and I think this works
#I now know that the counter a control variable for the loop,
#So I used a while loop to make sure it doesn't exceed the number input into the list

#So I didn't want to break what I wrote in the code so I'm going to write it here, but I did get confused...
#I used chat gpt to ask how I should use the counter variable and while I knew the first 2 lines, I don't get the 3rd 
#Just writing it so you are aware

counter = 0 # setting up chalk and a chalkboard to write tally marks
while counter < list_size: # every time I loop, I check if the amount of tally marks is equal to or more than list_size, in which case I stop
    num_input = input(f"Enter integer\n").strip()
    counter = counter + 1 # add a tally mark

    #I know that the f"" function makes it a script I just don't understand why we are adding 1 to the counter
    #I know this was in the lesson too and I looked it up but i want clarification

    #After this I need to make sure that the number input into the list is a valid number 

    while not num_input.isdigit():
        print(f'Error: {num_input} is NOT a number')
        num_input = input(f"Please enter a valid number")

    
    my_list.append(int(num_input))
    print(my_list)

#We have a list/scoresheet of things we want to add 
#Tally the number of items that are in the set 
#Add the first number to the second number, then that sum to the third number, then that sum to the fourth...

# counter = 0 # we set some sort of counter to 0
# # the counter tells the computer how many times it has done the loop
# # it is not smart, else it will forget and keep doing it over and over again

# running_total = 0

# while running_total < list_size: # repeat X times, where X is the size of the threshold
#     my_input # increment counter
    
#     # add code here
#     print(counter)

# APPROACH 1
# this works pretty well, but breaks if we have less than 2 items in the list
# that's cuz you can't add the first two items, if there aren't two items

# start by adding the first two numbers
running_total = my_list[0] + my_list[1]

counter = 0
while counter < list_size - 2:
    # when counter is 0, we want to add the third number, or index 2
    # when counter is 1, we want to add the fourth number, or index 3
    # when counter is N, we want to add the ???? number, or index 
    running_total = running_total + my_list[counter + 2]

    counter += 1

print(running_total)

# length of list is 3, but threshold should be 1
# length of list is 5, but threshold should be 3
# length of list is 6, but threshold should be 4
# length of list is 2, but threshold should be 0
# length of list is N, but threshold should be N-2

# APPROACH 2
# because we separated out the indexing to never use constants
# ie 
# we don't use my_list[1] or anything like that
# indexing is safer if you always make it dependent on the size of the list
# in this case, counter will never exceed the last index, so it'll never
# go past the end of the list

running_total = 0

counter = 0
while counter < list_size:

    my_list[counter] # this is basically accessing the "counterth" element in the list
    # ie, if counter is 0, its the first element
    # if counter is 1, its the second element

    running_total = running_total + my_list[counter] 
    counter += 1

print(running_total)


# APPROACH 3
# when you access each item in a list this way, consider a for loop

running_total = 0
for item in my_list: # this creates a new variable item, which will be the value of the Nth item in the loop, for each N in 1..length
    running_total += item

print(running_total)