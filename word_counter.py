word = input()
n = int(input())
counter = 0
for i in range(0,n):
    new_word = input()
    if new_word == word:
        counter+= 1
print(f'{word} is found {counter} times.')
