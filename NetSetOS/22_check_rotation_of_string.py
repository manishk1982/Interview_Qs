# Print rotation of string

str = "NetSetOs"
rotation = 5

# Check if 2 strings are rotated or not
str = "NetSetOs"
r_str = "SetOsNet"

flag = False
if len(str) == len(r_str):
    for i in range(len(str)):
        str = str[1:] + str[0]
        if str == r_str:
            flag = True
            break

if flag:
    print(f'{str} and {r_str} are rotated strings')
else:
    print(f'{str} and {r_str} are not rotated strings!!!')


# Another way
str = "NetSetOs"
r_str = "SetOsNt"
new_str = str + str
if len(str) == len(r_str) and r_str in new_str:
    print(f'{str} and {r_str} are rotated strings')
else:
    print(f'{str} and {r_str} are not rotated strings!!!')
