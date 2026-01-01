age = 30
member = True

if age > 18:
    if member:
        print("Ticket price is $12.")
    else:
        print("Ticket price is $20.")
else:
    if member:
        print("Ticket price is $8.")
    else:
        print("Ticket price is $10.")



i = 0; 

# if condition 1
if i != 0:
    # condition 1
    if i > 0:
        print("Positive")
        
    # condition 2
    if i < 0:
        print("Negative")
else:
    print("Zero")        