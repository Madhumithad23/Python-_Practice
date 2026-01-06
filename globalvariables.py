msg = "Python is awesome!"

def display():
    print("Inside function:", msg)

display()
print("Outside function:", msg)


s = "Python is great!"

def fun():
    global s
    s += " GFG"   # Modify global variable
    print(s)
    s = "Look for GeeksforGeeks Python Section"  # Reassign global
    print(s)

fun()
print(s)