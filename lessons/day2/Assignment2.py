#Write a program that accepts a number from the user.
#If it is divisible by 3 but NOT divisible by 5, write "fizz"
#If its divisible by 5 but NOT by 3, write "buzz"
#If its divisible by 3 and 5 write "fizzbuzz"

#Gonna kinda write out my thought process here
#Step 1: Start by having a number value. So I set the variable "number" = an integer value of number put in console.

number = int(input('Enter a number\n'))

#the \n puts the input a space below the question string
# also known as the NEWLINE character
# it's like when you press enter when typing

False
True

#Step 2: If it is divisible by 3 but NOT divisible by 5, write "fizz"
#if (number // 3 and not number // 5):
  #  print ('fizz')
  #The above function did not seem to work.  I am not gonna lie I didn't see what I did wrong so I had to chat gpt check it.
  #According to ChatGPT, it said that I need to use the modulo operator in a way that I am unfamiliar with cause I was confused with it.
  #Looking back at the notes we made in "operators" I think that doing "number % 3 == 0" checks if its divisible by 3.
  #Same for number % 5 == 0 obviously lol

if (number % 3 == 0 and not number % 5 == 0):
    print ('fizz') 

#This seemed to work when I tried the number 9, so I am going to write similar functions for the next 2 steps.

if (number % 5 == 0 and not number % 3 == 0):
    print ('buzz')

#I think this works, but I am not sure if I am expediting this process or doing it wrong. 

if (number % 5 == 0 and number % 3 == 0):
    print ('fizzbuzz')

