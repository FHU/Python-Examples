# Strings, Lists, and Tuples are common sequences in python
# Sequences are iterable, but not everything that is iterable is a sequence
# like dictionaries.

string_var = 'Hello, my name is'
list_var = ['Chicken', 'Airplane', 'Soldier']

# Access individual members of a sequence by index (starts at 0 and counts up by 1)
print(f'This is the seventh item in our string: {string_var[6]}')
print(f'This is the second item in our list: {list_var[1]}')

# Can also slice a sequence:
print(string_var[2:6]) # This includes the character at index 2 and excludes the item at index 6
print(list_var[0:2])

# Sequnces can be iterated over:
for character in string_var:
    print(character, end=' ')
print()