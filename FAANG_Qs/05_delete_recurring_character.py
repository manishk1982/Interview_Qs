# Given a string as your input, delete any recurring character, and return the new string.

from collections import Counter
str1 = "mississippi"

count = Counter(str1)
print(f'{count=}')
print(f'Preserving the order: {"".join(count.keys())}')

print(f'Without preserving the order: {"".join(set(str1))}')
