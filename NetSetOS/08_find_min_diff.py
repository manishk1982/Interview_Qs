# Find minimum difference between two elements of Binary Tree

arr = [5, 32, 45, 4, 12, 18, 25]
arr.sort()

min_diff = 99999
for i in range(len(arr) - 1):
    cur_diff = arr[i + 1] - arr[i]
    if cur_diff < min_diff:
        min_diff = cur_diff

print(f'Min diff: {min_diff}')
