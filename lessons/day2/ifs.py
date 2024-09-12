# IF STATEMENT
# code in an if statment only runs, if some condition is true

if(True):
    print('this will always run!')

if(False):
    print('this will never run!')

if(3 > 5):
    print('3 is greater than five!')

if(3 < 5):
    print('3 is less than 5')


its_raining = True
i_have_an_umbrella = True
if(its_raining and i_have_an_umbrella):
    print('thank god I have an umbrella!')

# TASK
# Write a program that asks for a users name
# Store that users name to a variable
# Then if their name is Nasim say hi nasim
# if their name is Victor say bye victor

#Assignment 1 
#Step 1 - write program...
question = 'What is your name?'
name = input()

nasim = 'nasim'
victor = 'victor'


if(name == nasim):
    print('hi nasim')

#the above can also be written as:
# if(x == True):
#    print('hi nasim')
#x by itself in the "if" function implies that it is true

if(name == victor):
    print('bye victor')