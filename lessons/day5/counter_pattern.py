

# counter pattern

# think of this as REPEAT X TIMES

counter = 0 # we set some sort of counter to 0
# the counter tells the computer how many times it has done the loop
# it is not smart, else it will forget and keep doing it over and over again

THRESHOLD = 10 # we have some sort of threshold. In this case, I'm setting it to a constant value. But it could be anything.

while counter < THRESHOLD: # repeat X times, where X is the size of the threshold
    counter += 1 # increment counter

    # add code here
    print(counter)


# if we want to use while to iterate through a list, we should set the threshold to be the list's size


counter = 0 # we set some sort of counter to 0
my_list = [1, 2, 3]
THRESHOLD = len(my_list) # we have some sort of threshold. In this case, I'm setting it to a constant value. But it could be anything.

while counter < THRESHOLD: # repeat X times, where X is the size of the threshold
    counter += 1 # increment counter

    # add code here
    print(my_list[counter]) # this is where we are indexing the Nth item in the list, where N is the counter 

    # in this case, counter actually serves as an INDEX, so I would usually name it *index* instead