# Find Out Pairs with given sum in an array in python of time complexity O(n log n)- FACEBOOK,AMAZON

arr = [5, 7, 4, 3, 9, 8, 19, 21]
sum = 17

# Sort the array
arr.sort()
print(f'List after sorting: {arr}')

left = 0
right = len(arr) - 1
flag = False
while left <= right:
    if arr[left] + arr[right] == sum:
        flag = True
        break
    elif arr[left] + arr[right] < sum:
        left = left + 1
    else: right = right - 1

if flag:
    print(f'Found matching sum: {sum} with {arr[left]} & {arr[right]}')
else:
    print("Failed to find the matching sum")