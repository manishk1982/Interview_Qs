# Find Maximum & Minimum Element In list - P

arr = [63, 54, 98, 34, 89, 42, 18]
min = 999999
max = 0
for item in arr:
    if item < min:
        min = item
    elif item > max:
        max = item
    else:
        continue
print(f'In list: {arr} -- Maximum: {max}, Minimum: {min}')


# Using sort
arr.sort()
print(f'In list: {arr} -- Maximum: {arr[-1]}, Minimum: {arr[0]}')
