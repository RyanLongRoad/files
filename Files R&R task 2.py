with open("students.txt", mode = "a", encoding="utf-8") as students:

    choice = 1


    while choice != "-1":

        new_name = input("Enter the name you wish to add to the list: ")    

        students.write("{0} \n".format(new_name))

        choice = input("Enter '-1' to end or 1 to continue:")

    

with open("students.txt", mode="r", encoding="utf-8") as students:
    number = 1
    for line in students:
        print("{0}. {1}".format(number, line))
        number = number + 1


