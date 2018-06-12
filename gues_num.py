import random
n = 0
checker = True
counter = 0
while checker == True:
    n = random.randint(1,10)

    if counter == 0:
        print(f'First number is: {n}')

    if counter >= 1:
        user = input("Up or Down: ")
        if (user == "down" and n < old_n )or (user == "up" and n > old_n):
            checker = True
            print(f'correct number is : {n}')

        else:
            print(f'Wrong number is: {n}')
            checker = False
    counter += 1
    old_n = n
