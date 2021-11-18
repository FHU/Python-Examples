'Use the debugger to see what happens with each call to sig_wins'
import copy

def sig_wins(all_wins):
    'function to modify the dictionary (mutable) passed'
    all_wins['EP'] += 1
    all_wins['list'][0] = 'one'
    return

if __name__ == "__main__":
    makin_music_wins = {'list': ['hi', 'two', 'three'], 'XBX': 23, 'ON': 7, 'EP': 67, 'PKA': 68, 'XCD': 30, 'Brotherhood': 1}
    sig_wins(makin_music_wins) # Mutability matters!
    sig_wins(makin_music_wins.copy()) # shallow copy (only copies the dictionary to a new object)
    sig_wins(copy.deepcopy(makin_music_wins)) # copy all the mutable objects in the data structure
    pass
