age = 16
p = False 

if age >= 18 or p:
    print("Access granted")
else:
    print("Access denied")

a = 55
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# break the loop as soon it sees 'k'
# or 'f'
i = 0
s = 'geeksforgeeks'

while i < len(s):
    if s[i] == 'k' or s[i] == 'f':
        i += 1
        break

    print(s[i])
    i += 1

user = ""
cur_user = user or "Guest"

print(cur_user) # when user is empty

user = "geeks"
cur_user = user or "Guest"  # when user in not empty

print(cur_user)            