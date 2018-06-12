n = int(input())
max_n = - 10000000000
for i in range(0, n):
    num = float(input())
    if num >= max_n:
        max_n = num

print(f'Max is: {max_n}')