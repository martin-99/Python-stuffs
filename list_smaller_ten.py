user_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
numbers_smaller_ten = []
for number in user_list:
    if number < 10:
        numbers_smaller_ten.append(number)
print(numbers_smaller_ten)