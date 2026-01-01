s = "geek"
print(not s)

a = [1, 2, 3, 4]
print(not a)

d = {"geek": "sam", "collage": "Mit"}
print(not d)

es = ""
print(not es)

el = []
print(not el)

ed = {}
print(not ed)


a = [5, 10, 20, 59, 83]
if not a:
    print("Inputted list is Empty")
else:
    for i in a:
        if not(i % 5):
            if i not in (0, 10):
                print(i,"is not in range")
            else:
                print(i, "in range")
        else:
            print(i,"is not multiple of 5")