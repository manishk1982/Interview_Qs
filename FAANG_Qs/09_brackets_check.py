# Grammarly type words and statements checking algo

line = "In cas{e of th[is} a](rgume)nt list, all argum}ents [are] (equally) impo[rtant"
print(f'input List: {line}')

brace_dict = {'}': '{',
              ']': '[',
              ')': '('}

braces_list = []
flag = True
for char in line:
    if char in ['[', '{', '(']:
        # Opening braces - add to the list
        braces_list.append(char)
    elif char in [']', '}', ')']:
        # Found closing brace - check for its subsequent opening pair
        if braces_list[-1] == brace_dict[char]:
            # Found the matching pair, pop from the list
            braces_list.pop()
        else:
            # Matching pair missing, quit and report
            flag = False
            break

if braces_list:
    print("ERROR: Line is not written as per Grammar rules")
else:
    print("SUCCESS: Line is written as per Grammar rules")
