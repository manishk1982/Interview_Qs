# WAVE ARRAY - DS & ALGO WITH PYTHON CODE -AMAZON,GOOGLE,ADOBE INTERVIEW QUESTION

# arr = [5, 1, 3, 2, 4]
# arr = [2, 4, 6, 5, 3, 8]
# arr = [5, 7, 8, 9, 20]
# arr = [3, 5, 12, 2, 6, 10, 7, 9, 8]
# Check if it is Wave Array or not
for arr in [[5, 1, 3, 2, 4], [2, 4, 6, 5, 3, 8], [5, 7, 8, 9, 20], [3, 5, 12, 2, 6, 10, 7, 9, 8]]:
    result = True
    for i in range(1, len(arr), 2):
        if arr[i - 1] > arr[i] and arr[i] < arr[i + 1]:
            pass
        else:
            result = False

    print(f'Result for {arr}: {result}')


# Convert to Wave array
arr = [3, 5, 12, 2, 6, 10, 7, 9, 8]
for i in range(0, len(arr), 2):
    if i != 0:
        if arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
    if i != len(arr) - 1:
        if arr[i] < arr[i + 1]:
            arr[i + 1], arr[i] = arr[i], arr[i + 1]

print(f'Converted Wave Array: {arr}')


# ANOTHER WAY -- Convert to Wave array
arr = [3, 5, 12, 2, 6, 10, 7, 9, 8]
for i in range(0, len(arr), 2):
    if i > 0 and arr[i - 1] > arr[i]:
        arr[i - 1], arr[i] = arr[i], arr[i - 1]
    if i < len(arr) - 1 and arr[i] < arr[i + 1]:
        arr[i + 1], arr[i] = arr[i], arr[i + 1]

print(f'Converted Wave Array: {arr}')
