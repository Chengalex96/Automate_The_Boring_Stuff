print('Enter a number: ')
first = int(input())
print('Enter a number: ')
second = int(input())
print('Enter a number: ')
third = int(input())
print('The sum is ' + str(first + second + third)) # Numbers are strings

# lets you run 1 line of code at a time, shows the variable values
# Over, step, out, go, breakpoints

import random

heads = 0

for i in range(1000):
    if random.randint(0, 1) == 1:
        heads = heads + 1
    if i == 500:
        print('halfway there') # setup breakpoint

print("Heads came up: " + str (heads))