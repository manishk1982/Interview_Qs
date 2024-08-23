# print("hello")

"""
# Input:

# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""


def find_max_gain(prices):
    max_gain = 0
    prince_count = len(prices)
    for i in range(prince_count - 1):
        for j in range(i + 1, prince_count - 1):
            current_gain = 0
            if prices[i] < prices[j]:
                current_gain = prices[j] - prices[i]

            if current_gain > max_gain:
                max_gain = current_gain

    return max_gain


prices = [7, 1, 5, 3, 6, 4]
print(f'Max gain: {find_max_gain(prices)}')
