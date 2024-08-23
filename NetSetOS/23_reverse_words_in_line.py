# Reverse order of Words in a line
line = "NetSetOS is an online educational platform"
print(f'Original line: {line}')

words = line.split(" ")
print(f'Reversed line: {" ".join(words[::-1])}')


# Reverse Words along with order in a line
reverse_line = [word[::-1] for word in words[::-1]]
print(f'Reversed line with reversed words: {" ".join(reverse_line)}')
