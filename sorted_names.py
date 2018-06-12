#Getting input which define how much name we will read from user
n = int(input())
#declarate empty list which will contain names
names = []
# for loop for each name
for i in range(0,n):
    new_names = input()
#append new name to a list of names
    names.append(new_names)
#sort all names
names.sort()
print("Sorted names are:")
#print all names
for name in names:
    print(name)
