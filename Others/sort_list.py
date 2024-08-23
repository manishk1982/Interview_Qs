# Sorting function without using the list.sort function

l1 = [76, 23, 45, 12, 54, 9]
print("Original List:", l1)

for i in range(len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] > l1[j]:
            l1[i], l1[j] = l1[j], l1[i]

print(f'Sorted list: {l1}')


# Another way
l1 = [76, 23, 45, 12, 54, 9]
print("Original List:", l1)

sorted_list = []
while l1:
    minimum = min(l1)
    sorted_list.append(minimum)
    l1.remove(minimum)

print(f'Sorted list: {sorted_list}')
