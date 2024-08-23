# Find out common letters between two strings Using Python

# s1 = input("Enter the first string: ")
# s2 = input("Enter the second string: ")

s1 = "NAINA"
s2 = "REENE"

print(s1, s2)

# Using set
print(f'Common letter: {set(s1).intersection(set(s2))}')

# Using &
str1 = set(s1)
str2 = set(s2)
print(f'Common letter: {str1 & str2}')
