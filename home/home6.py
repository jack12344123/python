def cal():
    num1 = float(input("Enter a number: "))
    op = input("Enter + / * - ")
    num2 = float(input("Enter another number: "))
    if op == "-":
        print(num1 - num2)
    elif op == "+":
        print(num1 + num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)


cal()



