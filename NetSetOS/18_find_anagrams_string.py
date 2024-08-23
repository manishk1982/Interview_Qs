# AMAZON INTERVIEW SERIES #1 Find the index of Groups of strings that are ANAGRAMS

word1 = "Fried"
word2 = "Fired"

word1_lst = [s for s in word1]
word2_lst = [s for s in word2]
word1_lst.sort()
word2_lst.sort()
if "".join(word1_lst) == "".join(word2_lst):
    print(f'{word1} and {word2} are Anagrams')
else:
    print(f'{word1} and {word2} are not Anagrams!!!')


# Print index o Anagrams words in the list
word_lst = ['cat', 'dog', 'odg', 'tca', 'act']
result = {}
idx = 0
for i in range(len(word_lst)):
    word = "".join(sorted(word_lst[i]))
    if word in result:
        result[word].append(i)
    else:
        result[word] = [i]

print(result)
