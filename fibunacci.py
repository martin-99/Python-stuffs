n = int(input("How many numbers do yo need:"))
index = int(input("which index: "))

def getting_number(x,y):
    z = x+y
    return z
def fibonacci(count,index):
    number = 1
    numbers = []
    for i in range(0,count):
        if i != 0:
            number = getting_number(numbers[i-1],numbers[i-2])
            numbers.append(number)

        else:
            numbers.append(number)
    return numbers[index-1]

print(fibonacci(n,index))

