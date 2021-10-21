'''tuple unpacking is a way of getting more than one object out of a function
technicall, you are returning one object (a tuple) and immediatly assigning
the values in the tuple to variables'''

def tuple_return_function():
    # for demonstration, we have a tuple with 3 different objects
    my_tuple = (27, 'hello', ['this', 'is', 'a', 'list'])
    # return one object
    return my_tuple 

# unpack the tuple into variables we can use
val1, val2, val3 = tuple_return_function()
print(f'The first object in my tuple is: {val1}')
print(f'The second object in my tuple is: {val2}')
print(f'The third object in my tuple is: {val3}')