# AN ALTERNATIVE APPROACH
# both are equally valid, just a slightly different logic

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

counter = 0
for the_guy_im_looking_at_rn in my_list:
    if the_guy_im_looking_at_rn % 3 == 0:
        counter = counter + 1

    if counter == 3:
        print(the_guy_im_looking_at_rn)
        break # stops the for loop, since we don't need to continue looking