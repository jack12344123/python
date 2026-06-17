def score():
    scores = []

    for i in range(1, 5):
        while True:
            mark = int(input(f"score {i}: "))
            if mark < 0 or mark > 100:
                print("try again to low or high")
            else:
                scores.append(mark)
                break
    average = sum(scores) / len(scores)
    print("Average:", average)
    if min(scores) >= 50:
        print("pass")
        if average >= 80:
            print("A")
        elif average >= 60:
            print("B")
        elif average >= 50:
            print("C")
        else:
            print("F")


score()