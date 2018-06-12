n = int(input())
counter = 0
numbers = []
for i in range (0,n):
    number = int(input())
    if number%2==0:
        counter+= 1
        numbers = numbers + [number]

print(f'Count of evens: {counter}')
print("Evens are:")
for num in numbers:
    print(num)
