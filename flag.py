f = False   # flag variable
a = [1, 3, 5, 7, 9]

for i in a:
    if a == 5:
        f = True
        break

if f:
    print("Number found!")
else:
    print("Number not found.")