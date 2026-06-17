def print_result():
    passed_count = 0
    scores = []

    for i in range(1, 5):
        while True:
            mark = int(input(f"score {i}: "))
            name = input("name")
            if mark >= 80:
                print(f"name:  : {mark}")
                print(name.upper())
                passed_count += 1
                print("passed")
                scores.append(mark)
                print(passed_count)

            else:
                print("failed")
                print(passed_count)

    print(passed_count)



print_result()
