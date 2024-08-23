# Print rotation of string

str = "NetSetOs"

rotation = 5

for i in range(rotation):
    str = str[1:] + str[0]
    print(f'Rotation: {i + 1}: {str}')


# Another way - by concatenating str by itself
print("Another way - by concatenating str by itself")
str = "NetSetOs"
length = len(str)
str = str + str
for i in range(rotation):
    print(f'Rotation: {i + 1}: {str[i:i + length]}')
