a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
user_list = []
input_user = int(input())
for number in a:
    if number < input_user:
        user_list.append(number)
print(user_list)