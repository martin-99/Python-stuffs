user_number = int(input())
list_numbers = []


def divisior (number):
     for i in range(2,number-1):

        if number%i==0:
            list_numbers.append(i)
     return list_numbers

