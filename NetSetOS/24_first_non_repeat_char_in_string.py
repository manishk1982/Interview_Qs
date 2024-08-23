# AMAZON CODING INTERVIEW QUESTION - FIRST NON-REPEATING CHARACTER IN A STRING (LeetCode)

s = "NETSETOSNET"
flag = False
for ch in s:
    if s.count(ch) == 1:
        flag = True
        break

if flag:
    print(f'First non-repeating char: {ch}')
else:
    print("None of the char is non-repeating!!!")


# Another way -- Return all non-repeating chars
from collections import Counter

result = Counter(s)
print(f'Non-repeating char(s) are: {[ch for ch in result if result[ch] == 1]}')
