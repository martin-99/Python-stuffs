birtday_dictionaries = {
    "Ariana Grande": 'June 26, 1993',
    "Selena Gomez": 'July 22, 1992',
    "Cristiano Ronaldo ": 'February 5, 1985',
}
print("Welcome to the birthday dictionary. We know the birthdays of: ")
for key in birtday_dictionaries:
    print(key)
user_choice = input('\n')
selected_element = birtday_dictionaries[f'{user_choice}']
print(f'{user_choice}\'s birthday is {selected_element}' )