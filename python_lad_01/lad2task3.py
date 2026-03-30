print("Insert card ")
card_number = input("Insert card number ")
if card_number != "1234":
    print("incorrect")
else:
    print("correct")
    withdraw = int(input("Insert withdraw amount "))
    if withdraw >= 1000:
        print( "insufficient funds")
    else:
        print("displaying funds")
        print("printing receigt")
        print("take your money")


