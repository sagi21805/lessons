while True:
    x = input("enter your password\n")
    if x == "1234":
        print("you may now enter!")
        break
    else:
        print("Wrong password, try agian.")
while True:
    x = input("enter a number\n")
    if x == "quit":
        break
    else:
        y = input("enter a number\n")
        if y == "quit":
            break
        else:
            x = int(x)
            y = int(y)
            print("x is:", x,"y is ", y)
            x = x - y
            y = y + x
            x = y - x
            print("x is:", x,"y is:", y)
    
        