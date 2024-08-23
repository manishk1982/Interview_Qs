# Amazon Interview question :- Roman Numerals to Integers

roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

for roman in ["LXVI", "LXIV", "CXLLIVI", "CXLVI"]:
    num = 0
    length = len(roman)
    i = 0
    while i < length:
        if i != length - 1 and roman_dict[roman[i]] < roman_dict[roman[i + 1]]:
            num += roman_dict[roman[i + 1]] - roman_dict[roman[i]]
            i += 1
        else:
            num += roman_dict[roman[i]]
        i += 1
    print(f'Roman: {roman} -- Integer: {num}')
