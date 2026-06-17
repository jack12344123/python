trise = 3

while True:
    password = input("enter your password: ")
    if password  == "king":
        print("you are a king")
        break
    else:
        print("please enter your password")
        trise -= 1
        if trise == 0:
            print("go away")
            break














