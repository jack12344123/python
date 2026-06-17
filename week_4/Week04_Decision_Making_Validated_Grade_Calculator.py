score = int(input('score: '))
while score < 0 or score > 100:
    print("not score")
    score = int(input('score: '))
    if score <= 100:
        print("right score")

if score >= 80:
    print("A")
elif score >= 60:
    print("B")
elif score >= 50:
    print("C")
else:
    print("f")


