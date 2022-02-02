import re

word_counts= {}
total_word_count = 0
one_big_list_o_words = []
with open("bible.txt") as bible:
    for line in bible:
        one_big_list_o_words.extend(re.sub(r'[.,:;?!()]','', line).lower().split())
        for word in re.sub(r'[.,:;?!()]','', line).lower().split():
            total_word_count += 1
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

print(f'The word "word" occurs {word_counts["word"]} times')
print(f'The word "word" occurs {one_big_list_o_words.count("word")} times')
print(f'There are {total_word_count} words in this bible')
print(f'The prob "word" is your randomly chosen word is {word_counts["word"]/total_word_count}')

print(f'Max: {max(one_big_list_o_words, key=len)} Min: {min(one_big_list_o_words, key=len)}')