# ================= PYTHAGOREAN THEOREM PROGRAM ==================
# a^2 + b^2 = c^2

a = int(input('type a: '))
b = int(input('type b: '))
# ....
# ....

c = (a ** 2 + b ** 2) ** 0.5 # x ** 0.5 is the same as taking the square root of x
print('c is:', c) # A comma inside the print thing means "print both of these things". More on that later


# ======================== FOOD PROGRAM ===========================

# Notice that `food` always takes the value of whatever was most recently set to it
# Remember that the code runs from top to bottom, so "most recently" is usually whatever is closest above it

food = input("what's your favourite food? ") # `food` is set to be whatever the user types in
print('I love', food)

food = 'pasta' # `food` is replaced with 'pasta'
print('I also love', food)

food = input('another one? ') # `food` is replaced with the user input
print('but my favourite is', food)
