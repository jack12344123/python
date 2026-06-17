def cal():
    num_1 = float(input("enter first number: "))
    op = input("enter operation - + / * ")
    num_2 = float(input("enter second number: "))
    if op == "+":
        print(num_1 + num_2)
    elif op == "-":
        print(num_1 - num_2)
    elif op == "*":
        print(num_1 * num_2)
    elif op == "/":
        print(num_1 / num_2)
cal()