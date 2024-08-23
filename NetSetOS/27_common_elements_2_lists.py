# INTERVIEW QUESTION - Find out elements common in two lists using Dictionary

l1 = [40, 50, 60, 80]
l2 = [50, 100, 150, 200]

# Using set
l1_set = set(l1)
l2_set = set(l2)

print(f'List1: {l1} & List2: {l2}')
print(f'Common element(s) using Set: {list(l1_set.intersection(l2_set))}')


# Using list traversal
result = []
for item in l2:
    if item in l1:
        result.append(item)
print(f'Common element(s) using List Traversal: {result}')


# Using list traversal - thru list comprehension
result = [item for item in l2 if item in l1]
print(f'Common element(s) using List Traversal & list comprehension: {result}')


# Using dictionary
from collections import Counter
l1_cnt = Counter(l1)
result = []
for item in l2:
    if item in l1_cnt:
        result.append(item)
print(f'Common element(s) using dictionary: {result}')
