# Python program to implement a Binary Search

arr = [1, 2, 4, 5, 6, 7, 9, 12]

begin = 0
end = len(arr) - 1

# Number to looked for
num = 4

flag = False
while begin < end:
    mid = begin + end // 2
    if arr[mid] == num:
        flag = True
        print(f'Found element at position {mid}')
        break
    elif num < arr[mid]:
        end = mid
    else:
        begin = mid

if not flag:
    print(f'Failed to number {num} in the list {arr}')


# Another way
begin = 0
end = len(arr) - 1
mid = begin + end // 2

while begin < end and arr[mid] != num:
    if num < arr[mid]:
        end = mid
    else:
        begin = mid
    mid = begin + end // 2

if arr[mid] == num:
    print(f'Found element at position {mid}')
else:
    print(f'Failed to number {num} in the list {arr}')
