#  Python Program to print Prime Numbers between 2 numbers

for num in range(100, 200):
    flag = False
    for i in range(2, num):
        if num % i == 0:
            flag = True
            break

    if flag is False:
        print(f'{num} is prime number')


# Another way
print("\n\nAnother way...")
for num in range(100, 200):
    print([num % i != 0 for i in range(2, num)] )
    print(all(num % i != 0 for i in range(2, num)))
    if all(num % i != 0 for i in range(2, num)):
        print(f'{num} is prime number')


print("\n\n###########")
print(all([False, False, False, True]))
print(all([True, True, True, True]))