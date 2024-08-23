# Find maximum difference between two elements of Binary Tree

arr = [5, 32, 45, 4, 12, 18, 25]
arr.sort()

max_diff = 0
for i in range(len(arr) - 1):
    cur_diff = arr[i + 1] - arr[i]
    if cur_diff > max_diff:
        max_diff = cur_diff

print(f'Max diff: {max_diff}')
