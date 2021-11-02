# investigate Python's object reuse with the is operator
import copy

name = 'Bob'
name2 = 'Bob'

print(id(name))
print(id(name2))

if name == name2:
    print('Name equal')
else:
    print('Name not equal')

# Are these the same object?
if name is name2:
    print('name and name2 are the same Object!')
else:
    print('name and name2 are not the same Object')

# Print a line to differentiate outputs a little more
print('----------------------------------------')

# copy is useful for making sure you use a different object,
# but it doesn't make sense for an immutable data type
name3 = 'Alice'
name4 = copy.copy(name3)

print(id(name3))
print(id(name4))

if name3 == name4:
    print('Name equal')
else:
    print('Name not equal')

# Are these the same object?
if name3 is name4:
    print('name3 and name4 are the same Object!')
else:
    print('name3 and name4 are not the same Object')

# Print a line to differentiate outputs a little more
print('----------------------------------------')

names = ['Bob', 'Alice']
names2 = ['Bob', 'Alice']

print(id(names))
print(id(names2))

if names == names2:
    print('Names equal')
else:
    print('Names not equal')

# Are these the same object?
if names is names2:
    print('names and names2 are the same Object!')
else:
    print('names and names2 are not the same Object')

# Print a line to differentiate outputs a little more
print('----------------------------------------')

names = ['Bob', 'Alice']
names2 = names

print(id(names))
print(id(names2))

if names == names2:
    print('Names equal')
else:
    print('Names not equal')

# Are these the same object?
if names is names2:
    print('names and names2 are the same Object!')
else:
    print('names and names2 are not the same Object')

# Print a line to differentiate outputs a little more
print('----------------------------------------')

# You can use the copy module to make copies of objects explicitly
# if you have a mutable object inside the copied object, this may not be enough.
# copy.deepcopy is similar for nested objects.
names = ['Bob', 'Alice']
names2 = copy.copy(names)

print(id(names))
print(id(names2))

if names == names2:
    print('Names equal')
else:
    print('Names not equal')

# Are these the same object?
if names is names2:
    print('names and names2 are the same Object!')
else:
    print('names and names2 are not the same Object')