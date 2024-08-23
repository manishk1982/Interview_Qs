# Write a Python Program to rotate the elements given in a list to the left

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(f'List before rotation: {arr}')

count = 8

for i in range(count):
    val = arr[0]
    arr.remove(val)
    arr.append(val)

print(f'List after rotation: {arr}')


print("Another better & efficient way ---")
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(f'List before rotation: {arr}')

new_arr = arr[count:] + arr[:count]
print(f'List after rotation: {new_arr}')
