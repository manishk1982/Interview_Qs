# Conversion of two list into Dictionary

list1 = [1, 2, 3]
list2 = ["one", "two", "three"]

# Using loop
result = {}
for key, value in zip(list1, list2):
    result[key] = value
print(f'Output Dictionary: {result}')


# Using Dict
print(f'Output Dictionary: {dict(zip(list1, list2))}')

