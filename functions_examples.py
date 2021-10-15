# function definition minimum
def function_name():
  pass # your code goes in this codeblock
       # return None is implied here

# function call minimum
function_name() #this does nothing, but it runs

# function with parameters
def func_with_param(param1, param2):
  return_value = str(param1) + ' ' + str(param2) # string concatination
  return return_value

# function call with hardcoded values passed as arguments
new_string = func_with_param('Steve', 'Cheetoes')

# function definition with type hints. This function takes 3 strings and returns an integer
def vol_of_box(height:str, width:str, length:str) -> int:
    value = int(height) * int(width) * int(length)
    return value

# function call for vol_of_box
def use_vol_of_box():
    h = input()
    w = input()
    l = input()
    volume = vol_of_box(h,w,l)
    assert isinstance(volume, int)
    print(volume)