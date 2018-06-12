n = int(input())
names = []
for i in range(0,n):
    new_names = input()
    names.append(new_names)
names.sort()
print("Sorted names are:")
for name in names:
    print(name)
