'''
Given num_rows and num_cols, print a list of all seats in a theater. 
Rows are numbered, columns lettered, as in 1A or 3AE. Print a space after 
each seat.

Sample output with inputs: 2 3

When you run out of letters, use AA - ZZ. So, the first seat will be
1A and the last possible column would be 1ZZ.
1AA
1AB
1AC
'''

num_rows = int(input())
num_cols = int(input())

# This solution uses string slicing
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for x in range(1,num_rows +1):
    for y in alphabet[0:num_cols]:
            print(f'{x}{y}', end=' ')
print()

# This solution works through column ZZ
for x in range(1,num_rows + 1):
    for y in range(0, num_cols):
        if y < 26:
            print(f'{x}{chr(65 + y)}', end = ' ')
        else:
            letter1 = chr(64 + y // 26)
            letter2 = chr(65 + y % 26)
            print(f'{x}{letter1}{letter2}', end = ' ')

print()

# This solution works for any number of rows and columns
for x in range(1,num_rows + 1):
    for y in range(0, num_cols):
        column = ''
        while y >=0:
            column += chr(65+((y) % 26))
            y = (y // 26) - 1
        print(f'{x}{column[::-1]}', end = ' ')

print()