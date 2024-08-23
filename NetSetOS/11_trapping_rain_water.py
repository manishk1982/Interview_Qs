# TRAPPING RAIN WATER

arr = [1, 0, 2, 0, 1, 0, 3, 1, 0, 2]

length = len(arr)
left = []
left.append(arr[0])
for i in range(1, length):
    if left[i - 1] < arr[i]:
        left.append(arr[i])
    else:
        left.append(left[i - 1])
print(left)

right = []
right.append(arr[-1])
for i in range(length - 2, -1, -1):
    if right[0] < arr[i]:
        right.insert(0, arr[i])
    else:
        right.insert(0, right[0])
print(right)

cnt = 0
for i in range(length):
    # Maybe cna do this directly
    # cnt += min(left[i], right[i]) - arr[i]
    min_val = min(left[i], right[i])
    if min_val > arr[i]:
        cnt += min_val - arr[i]

print(f'Answer: {cnt}')
