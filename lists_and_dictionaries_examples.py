# basic list
list_var = ['one','two','three']

# basic tuple
tuple_var = (1,2,3)

# singe item in list
print(f'The second item in our list is {list_var[1]}')

# iterate over every item in a list
for item in list_var:
    print (item)

# using enumerate()
# list_var = ['one','two','three']
# (0,'one')
# (1, 'two')
# (2, 'three')
for index, value in enumerate(list_var):
    print(f'Value {value} is at index {index}')

# basic dictionary
dictionary_var = {'word': 'definition',
                  'word2': 'definition2',
                  'word3': 'definition3'}

# referce dictionary value by key
print(dictionary_var['word'])

for word, definition in dictionary_var.items():
    print(f'{word} - {definition}')

for definition in dictionary_var.values():
    print(definition)

list_of_lists = [[1,2,3], [4,5,6], [7,8,9],
                 [12,13,14], [15,16,17]]

print(list_of_lists[1][2])

from box_volume import vol_of_box
# dictionary of lists
dictionary_of_lists = {'box1': [2,3,4],
                  'box2': [5,6,7],
                  'box3': [8,9,10]}

for box_name, measurements in dictionary_of_lists.items():
    h, l, w = measurements
    print(f'The {box_name} volume is {vol_of_box(h,l,w)}')

# dictionary of dictionaries
dictionary_of_dictionaries = {'box1': {'h':2,'l':3,'w':4},
                              'box2': {'h':5,'l':6,'w':7},
                              'box3': {'h':8,'l':9,'w':10}}

for box_name, measurements in dictionary_of_dictionaries.items():
    volume = vol_of_box(measurements['h'],measurements['l'],measurements['w'])
    print(f'The {box_name} volume is {volume}')
