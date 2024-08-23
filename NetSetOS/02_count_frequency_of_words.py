# Count the frequency of words appearing in a string

from collections import Counter

line = "Sheena loves eating Mango and Apple. Her sister also loves eating Mango and Apple"
print(f'Input line: {line}')

word_list = line.split()


# Using loop
result = {}
for word in word_list:
    result[word] = result.get(word, 0) + 1

print(f'Count: {result}')


# Using collections.Counter() to get count
result = Counter(word_list)
print(f'Count: {result}')
