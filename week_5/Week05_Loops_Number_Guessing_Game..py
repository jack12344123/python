secret = 7
number = int(input("Enter a number: "))
while number != secret:
    if number > 7:
        print("to high")
        number = int(input("Enter a number: "))
    if number < 7:
        print("to low")
        number = int(input("Enter a number: "))
if number == secret:
    print("good job")

