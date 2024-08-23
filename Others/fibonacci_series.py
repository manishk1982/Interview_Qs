# Python program to print Fibonacci Series

a = 0
b = 1
fibo = [a, b]
for i in range(2, 10):
    fibo.append(a + b)
    a, b = b, b + a

print(f'Fibonacci Series: {fibo}')


# Using recursion
def fibo_fx(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo_fx(num - 1) + fibo_fx(num - 2)


for i in range(10):
    print(f'Fibonacci Series: {fibo_fx(i)}')
