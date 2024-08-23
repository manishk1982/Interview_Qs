# Evaluate Postfix Expression using Stack

expr = ['2', '1', '+', '3', '*']

lst = []
for item in expr:
    if item.isdigit():
        # if item not in ['+', '*', '-', '/']:
        lst.append(int(item))
    else:
        num1 = lst.pop()
        num2 = lst.pop()

        match item:
            case '+':
                lst.append(num1 + num2)
            case '-':
                lst.append(num1 - num2)
            case '*':
                lst.append(num1 * num2)
            case '/':
                lst.append(num1 / num2)
            case '%':
                lst.append(num1 % num2)

print(f'Answer: {lst[0]}')

