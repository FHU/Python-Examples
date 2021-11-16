'''Example for printint dictionaries one line at a time'''

def print_dog_boarding(dogs: dict):
    'print all the dogs in their kennels'
    for location, name in dogs.items():
        print(f'{int(location):04d}: {name}')

def get_dog_names():
    'Populate the dictionary from user input'
    dog_name = ''
    dogs_boarded = {}
    while dog_name != 'done':
        kennel_id = input('Where is this dog staying (done to finish)? ')
        if kennel_id == 'done':
            break
        dog_name = input("What is the dog's name (done to finish)? " )
        dogs_boarded[kennel_id] = dog_name

    return dogs_boarded

if __name__ == "__main__":
    print_dog_boarding(get_dog_names())