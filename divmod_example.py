'''divmod() is a function that floor divides and mods at the same time'''

# Using floor divide and mod, we can calcluate how many dollars
# are in a stack of pennies like this:
pennies = 2345

dollars = pennies // 100
pennies = pennies % 100
print(f'dollars: {dollars} with {pennies} left over.')

# This is the functional equivalent using divmod()
pennies = 2345

dollars, pennies = divmod(pennies, 100)
print(f'dollars: {dollars} with {pennies} left over.')

# This is ugly, but still functionally equivalent:
returned_tuple = divmod(cents_from_user, 100)
print(returned_tuple)

dollars = returned_tuple[0]
remainder = returned_tuple[1]
