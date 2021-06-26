x = 42 # Assignment operator: We had covered this before

x < 50 # True: "Less Than" Operator
x > 50 # False: "Greater Than" Operator
x <= 50 # True: "Less Than Or Equal To" Operator
x >= 50 # False: "Greater Than Or Equal To" Operator

x == 50 # False: "Equal To" Operator
(x * 2) == 84 # True
x != 50 # True: "Not Equal To" Operator

word = input("What's your favorite word? ")
if word == 'poop': # Checks to see if `word` has the same value as `'poop'`
    print('I knew you liked poop') # If so, we run these 3 lines
    print('but how much do you like poop?')
    print('because I REALLY like poop.')
elif word == 'crap': # If not, check again to see if it has the same value as `'crap'`
    print('crap is cool')
    print('but not as cool as poop')
elif word == 'shit': # If not, check once more to see if it has the same value as `'shit'`
    print('shit is cool')
    print('but not as cool as poop')
else: # If nothing above matched, we do these lines
    print('oh.. you hate poop?')
    print('look at mister clean over here')
print('game over')

x = 0
while x < 5: # Run to following block as long as x is less than 5
    print('My number is', x)
    x = x + 1
print('Done!')


# Our previous homework assignment, but done more consicely. We are looping our
# program 3 times instead of just copying and pasting.
counter = 0
while counter < 3:
    name = input('Enter a name: ')
    poops_per_day = int(input('How many poops in a day? '))

    print('Looks like', name, 'poops at a rate of', poops_per_day/24, 'pph (poops per hour)')

    counter += 1 # counter = counter + 1


# THINGS TO REMEMBER!
# - Don't forget the colon after your `if` and `while` stuff
# - When using a `while` loop, make sure to see if the loop ends or not