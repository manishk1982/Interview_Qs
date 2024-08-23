# Analyze if a stock price has always gone up or always gone down

def check(arr):
    flag = None
    if arr[0] > arr[1]:
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                flag = "Dec"
            else:
                flag = None
                break
    else:
        for i in range(1, len(arr) - 1):
            if arr[i] < arr[i + 1]:
                flag = "Inc"
            else:
                flag = None
                break

    return flag


for arr in [[10, 9, 8, 7, 6, 5, 4], [10, 9, 8, 7, 6, 5, 4, 8], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 4]]:
    result = check(arr)
    if result == "Inc":
        print(f'For {arr}: Stock price has always gone up')
    elif result == "Dec":
        print(f'For {arr}: Stock price has always gone down')
    else:
        print(f'For {arr}: Stock price has gone both up & down')


print("Another better & efficient way ---", sep='\n')
for arr in [[10, 9, 8, 7, 6, 5, 4], [10, 9, 8, 7, 6, 5, 4, 8], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 4]]:
    if all([arr[i] < arr[i + 1] for i in range(len(arr) - 1)]):
        print(f'For {arr}: Stock price has always gone up')
    elif all([arr[i] > arr[i + 1] for i in range(len(arr) - 1)]):
        print(f'For {arr}: Stock price has always gone down')
    else:
        print(f'For {arr}: Stock price has gone both up & down')

line = "Another better & efficient way ---"
print(*line, sep='\n')
