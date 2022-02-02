# Python3 code to demonstrate working of
# Removing punctuations in string
# Using regex
import re

# initializing string
test_str = "Gfg, is best : for ! Geek's ;"

# printing original string
print("The original string is : " + test_str)

# Removing punctuations in string
# Using regex
res = re.sub(r'[^\w\s]', '', test_str)

# printing result
print("The string after punctuation filter : " + res)
