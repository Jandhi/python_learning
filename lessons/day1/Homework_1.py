# Write a program that does the following:
#STEP 1: Ask the user for their name.  Take their name from input.  Then ask the user for their age.  Take their age as input.

#1. Ask the user for their name.
question_1 = 'What is your name?'
print (question_1)

#2. Take their name from input
name = input()

#3.Then ask the user for their age.
question_2 = 'What is your age?'
print (question_2)

#4. Take their age from input.
age = input()

#STEP 2: Then print the following sentence:"Hello <x>, in 1 year, you will be <y> years old!

#1. Add a new variable called "future_age" that will be the integer of "age" variable + 1 
#this should help us when just trying to write the 'print' code
future_age = int(age) + 1

#2. Now we need to print the sentence outlined in step 2 
reply = 'Hello ' + name + ', in one year, you will be ' + str(future_age) + " years old!"
print (reply)


