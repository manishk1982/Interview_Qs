# Python Interview Question - Excel column number [ LEETCODE 171 ]

col_label = "BI"

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_count = {}
alphabet_multiplier = {}
for i in range(len(alphabets)):
    alphabet_count[alphabets[i]] = i + 1
    alphabet_multiplier[alphabets[i]] = (i + 1) * 26

# print(alphabet_count)
# print(alphabet_multiplier)

col_num = alphabet_count[col_label[-1]]
print(col_num)
if len(col_label) == 2:
    col_num += alphabet_multiplier[col_label[0]]

print(f'Column Label: {col_label} -- Column Number: {col_num}')
