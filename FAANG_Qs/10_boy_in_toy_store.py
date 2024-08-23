# The BOY in the TOY store

toy_prices = [1, 12, 5, 111, 200, 1000, 10, 4, 6]
money = 80
print(f'Toy prices original: {toy_prices}')

toy_prices.sort()
# toy_prices = sorted(toy_prices)
print(f'Toy prices after sorting: {toy_prices}')

toy_count = 0
for i in toy_prices:
    if money - i >= 0:
        toy_count = toy_count + 1
        money = money - i

print(f'Maximum number of toys that can be bought: {toy_count}')