s = ["Geeks", "for", "Geeks"]

# using for loop with string
for i in s:
    print(i)

s = "Geeks"
for i in s:
    print(i)

for i in range(0, 10, 2):
    print(i)

# Prints all letters except 'e' and 's'

for i in 'geeksforgeeks':

    if i == 'e' or i == 's':
        continue
    print(i)
                