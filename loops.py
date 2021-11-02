# Infinite loop (uncomment these two lines to see it)
# while True:
#    print('This is fun!!!', end =' ')

# Contrived use of a while loop
count = 0
while count < 200:
    print(f'This is fun {count}!!!', end =' ')
    count += 1

# functionally equivalent for loop
for number in range(0,200):
    print(f'This is fun {count}!!!', end =' ')

# more complicated expression in a while (still contrived)
count = 0
letter = 'y'
while count < 200 or letter != 'n':
    print(f'This is fun {count}!!!', end =' ')
    count += 1

    if count == 500:
        letter = 'n'

# using an input variable to trigger the end of a loop
# zyBooks calls this a sentinal value
user_input = ''
count = 0
total = 0
while user_input != 'q':
    user_input = input("Provide value ('q' to quit): ")

    if user_input.isnumeric():
        count += 1
        total += int(user_input)
    else:
        print('BAD NUMBER')

if count > 0:    
    print(f'count: {count} total: {total} avg: {total/count}')


# For example to iterate over an iterable
word = 'supercalifragilisticexpialidocious'

for letter in word:
    print(letter)