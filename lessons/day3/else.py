# ELSE AND ELIF

# IF you have an IF statement, we can use else to do something if it is
# NOT true


if 1 == 2:
    print('Mathematics has failed')
else:
    print('Math still works')

# EQUIVALENT TO

if 1 == 2:
    print('Mathematics has failed')
if not (1 == 2):
    print('Math still works')

# ELIF is what you do if you want "else if"

is_nasim = False
is_victor = True

if is_nasim:
    print('hey sexy')
elif is_victor:
    print('hey stinky')
else:
    print('who are you???')