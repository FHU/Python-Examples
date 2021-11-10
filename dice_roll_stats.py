import random
import matplotlib.pyplot as plt

# We are going to use a dictionary to keep our counts in this example 
roll_counts = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
num_rolls = int(input('Enter number of rolls:\n'))

if num_rolls >= 1:
    for i in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2

        #Count number of sixes and sevens
        roll_counts[roll_total] += 1
        print('Roll {} is {} ({} + {})'.format(i, roll_total, die1, die2))

    print('\nDice roll statistics:')
    for roll, roll_count  in roll_counts.items():
        hist = '*' * roll_count
        print(f'{roll}s {hist}')
else:
    print('Invalid number of rolls. Try again.')

plt.bar(roll_counts.keys(), roll_counts.values())
plt.show()