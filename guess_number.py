import random
random_num = random.randint(1,9)
checker = True
while checker == True:
    user_gues = int(input("Tell me your gues: "))
    if user_gues > random_num:
        print("Too Hight:")
    elif user_gues < random_num:
        print("Too Low")
    else:
        print("Congratulation number is guesed !")

        play_again = input("Do you want play again: Y/N ")
        if play_again == "y":
            checker = True
            random_num = random.randint(0,9)
        else:
            print("Good game come again")
            checker = False

