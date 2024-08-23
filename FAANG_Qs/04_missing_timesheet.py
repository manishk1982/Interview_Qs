# Factory workers fill in missing time entries

l1 = [1, 2, 3, None, 4, 5, None, 6, None, 7, None, 8, 9, None, None]
print("Original List:", l1)

for i in range(len(l1)):
    if l1[i] is None:
        l1[i] = l1[i - 1]

print(f'Filled list: {l1}')
