word = input()
word = str(word)
rvs = word[: : -1]
print(rvs)
if word == rvs:
    print(f'This word is Palindrom: {word}')
else:
    print(f'This word is not Palindrome: {word}')