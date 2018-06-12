import random
player_one = input("So what is your choice: rock , papper or scissors  ")
def rock_papper_scissors(user):
    check = True
    second_player = ["rock", "papper", "scissors"]
    while check == True:
        index = random.randint(0,2)
        second_player_choice = second_player[index]
        print(f'The Second player choose: {second_player_choice}')
        if user == "rock" and second_player_choice == "scissors":
            print(f'Winner is First Player with {user}')
        elif user == "papper" and second_player_choice == "rock":
            print(f'Winner is First Player with {user}')
        elif user == "scissors" and second_player_choice == "papper":
            print(f'Winner is First Player with {user}')
        elif user == second_player_choice:
            print(f'This battle is draw')
        else:
            print(f'Winner is Second  Player with: {second_player_choice}')
        question = input("Do you want to play again: Y/N ")
        if question == "y":
            check = True
        else:
            check = False
print(rock_papper_scissors(player_one))