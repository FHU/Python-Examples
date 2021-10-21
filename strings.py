name = 'Bob'

multiline_string1 = (f'''Hello {name}.
My name is Bingo!
I like to climb on things!\n''')

multiline_string2 = (f'Hello {name}.\n'
                      'My name is Bingo!\n'
                      'I like to climb on things!\n')

print(multiline_string1)

# String concatination
string1 = 'Hit!!'
string2 = 'You sunk my battleship!'
integer1 = 42

# print() does its best to print each object passed to it
# this is not the same as string concatination
print(string1, string2, integer1)
print(string1, string2, str(integer1))

# Use + with strings for concatination in Python
print(string1 + ' ' + string2 + ' ' + str(integer1))

# This line would raise a TypeError
# print(string1 + ' ' + string2 + ' ' + integer1)

string_concat = string1 + ' ' + string2 + ' ' + str(integer1)
#print(string_concat)

# f strings are not concatination, either
# even though this is functionally equivalent to the lines above
print(f'{string1} {string2} {integer1}')

# format method on strings with named variables
# you might want to use this if you are templating a long string
heights = {'Bob': '5\'7"', 'Alice': '9\'9"', 'Charlie': '2\'7"', 'Thumbalina': '0\'1"'}
format_string = '{name} is {height} tall'

for name_from_dict, height_from_dict in heights.items():
    print(f'{name_from_dict} is {height_from_dict} tall')
    #print(format_string.format(name_from_dict, height_from_dict))
    print(format_string.format(height = height_from_dict, name = name_from_dict))