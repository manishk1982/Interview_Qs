# Remove Duplicates from Sorted Array (With Algorithm & Python Code)

arr = [1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5]
# Without creating new array
print(f'Original: {arr}, Duplicates removed: {list(set(arr))}')


# With creating new array
result = []
for i in arr:
    if i not in result:
        result.append(i)

print(f'Original: {arr}, Duplicates removed: {result}')
