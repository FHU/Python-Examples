'''Branching and conditional statements are used to run different code
based on run-time criteria with if, if-else, if-elif, and if-elif-else'''

#basic if statment
condition = True

if condition == True:
    pass #run this code

# if-else
if condition != True:
    pass
else:
    pass #run this code

# use the in operator
names = ['Bob', 'Alice', 'Charlie']
user_input_name = input('Enter a name: ')

if user_input_name in names:
    print('Yay!')
else:
    print('Boo')