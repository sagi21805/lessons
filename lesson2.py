def password(x: str = None) -> str and bool:  
    if x == "1234":
        return True, print("success")
    else:
        return False
x = input("enter your password\n")
while password(x) == False:
    if len(x) != 4:
        print("Password must be 4 characters")
    else:
        print("Wrong password")  
    x = input("enter your password\n")