import random

#Assignment 3
#You receive a list of numbers.  Tell me what the third number divisible by 3 is
#So what I am going to do first is to build my list simply as below:

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
numbers_divisible_by3 = []

#"Tell me what the third number divisilble by 3 is"
#So to do this, we need to first pick out the third number from the set.

#item = my_list[2]
#if (item % 3 == 0):
    #print ('True')

#I was being a silly goose and forgot to use the 'for loop'
for num in my_list:
    if (num % 3 == 0):
        numbers_divisible_by3.append(num)
print(numbers_divisible_by3)
    
#Okay I will admit the only thing that I was unsure of here is why youy mentioned to use the append function.
#I remember that the append function lets us add numbers to the list, but I'm not getting really why it needs to be here...
#Could be wrong, but I think you want me to use the append function to add the numbers that are divisible by 3 into a new list
#I had to move it around like 6 times because the indents weren't working in case you're wondering why i'm typing here lol

#Not sure if I am stil supposed to do this because i can already see that the third number is 3 in the list in the console
#But I will do the following:


third_redhead = numbers_divisible_by3[2]
print(third_redhead)

# AN ALTERNATIVE APPROACH
# both are equally valid, just a slightly different logic

counter = 0
for the_guy_im_looking_at_rn in my_list:
    if the_guy_im_looking_at_rn % 3 == 0:
        counter = counter + 1

    if counter == 3:
        print(the_guy_im_looking_at_rn)
        break # stops the for loop, since we don't need to continue looking