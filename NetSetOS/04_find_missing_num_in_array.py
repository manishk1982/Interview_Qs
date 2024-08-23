# FIND MISSING NUMBER IN AN ARRAY(SUMMATION & X-OR)

# Summation method
arr = [1, 2, 4, 5, 6, 7]

summation = (arr[-1] * (arr[-1] + 1)) // 2
print(f'Summation: {summation}')

arr_sum = sum(arr)
print(f'Array sum: {arr_sum}')

print(f'Missing number using Summation: {summation - arr_sum}')


# XOR method
from functools import reduce


def xor_filter(a, b):
    return a ^ b


xor_arr = arr[0]
for i in range(1, len(arr)):
    xor_arr = xor_arr ^ arr[i]

xor_sum = 1
for i in range(1, arr[-1]):
    xor_sum = xor_sum ^ i
print(f'Missing number using XOR: {xor_sum - xor_arr}')

# Using reduce
xor_sum = reduce(xor_filter, list(range(2, arr[-1])))
print(f'Missing number using XOR: {xor_sum - xor_arr}')
