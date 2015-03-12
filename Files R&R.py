with open("students.txt", mode="r", encoding="utf-8") as students:
    number = 1
    for line in students:
        print("{0}. {1}".format(number, line))
        number = number + 1

