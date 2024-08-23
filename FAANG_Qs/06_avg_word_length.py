# Essay Exam Competition: Average Word Length in a statement

from functools import reduce


def total(len1, len2):
    return len1 + len2


line = "Hello, Python is my favorite language"

words = line.split()
char_count = reduce(total, map(lambda word: len(word), words))
avg = char_count / len(words)

print(f'Total char count: {char_count}')
print(f'Average char count: {avg}')


# Another way
avg = sum(len(word) for word in words)/len(words)
print(f'Average char count: {avg}')
