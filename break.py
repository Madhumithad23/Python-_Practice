matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
val = 5
found = False

for r in matrix:
    for n in r:
        if n == val:
            print(f"{val} found!")
            found = True
            break  # Exit the inner loop
    if found:
        break  # Exit the outer loop