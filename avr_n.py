check = True
while check == True:
    n = int(input())
    num = 0
    for i in range (0,n):
           new_num = float(input())
           num = num + new_num
           avg_num = num / n
    print(f'Avg is: {avg_num}')
    question= input("Do you want more: y/n:")
    if question == "y":
        check = True
    else:

        check = False

