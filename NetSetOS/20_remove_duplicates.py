# Remove Duplicates In Python

arr = [1, 4, 2, 5, 2, 3, 4, 1, 4, 5, 2, 3]

# Using set
print(f'Using set -- Original: {arr}, Result: {list(set(arr))}')


# Using array
result = []
for item in arr:
    if item not in result:
        result.append(item)
print(f'Using array -- Original: {arr}, Result: {result}')


# Using lamda
remove_dup = lambda lst: list(set(lst))
print(f'Using lambda -- Original: {arr}, Result: {remove_dup(arr)}')


# Using dict


# Using symmetric diff
set1 = {1, 2, 4, 5}
set2 = {2, 1, 5, 7}
result = []
for item in set1:
    if item not in set2:
        result.append(item)

for item in set2:
    if item not in set1:
        result.append(item)

print(result)