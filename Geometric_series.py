# Written by Thy H. Nguyen

num_1 = float(input ("Enter the first term of the series: "))
num_2 = float(input("Enter the second term of the series: "))
num_3 = float(input("Enter the third term of the series:  "))
num_4 = input("How many total terms are considered?  ")

if num_1 < num_2 < num_3 < num_4 :
    try:
        float(thuy) != 0
        float(thy) != 0

        try:
            value_1 = float(thy)
            value_2 = float(thuy)
            value_3 = float(thuyy)

            x = float(thuyy)/float(thuy)
            y = float(thuy)/float(thy)

            if x == y :
                print(thy, "is the first term of the geometric series ",
                  thuy, "is the second term of the geometric series",
                thuyy, "is the third term of the geometric series")
            else:
                print("This is not a geometric series!!!")

            if ans == "finite" and x!= 1 and x==y:
                print("The sum of this finite geometric series is: ", ((value_1)*(1-x**3))/(1-x))

            if ans == "infinite":
                print("b")

            if ans != "finite" and ans != "infinite":
                print('Please choose one, and only enter "finite" or "infinite!"')

        except ValueError:
            print("Please enter the value again. DO NOT ENTER FRACTIONS!!! DO NOT ENTER WORDS!!!")

    except ZeroDivisionError:
        print("The is not a geometric series. Try other methods to calculate the sum of the first n terms!")
else:
    print("This is not the first three terms (in a correct order) in a geometric series. Try other methods to calculate the sum of the first n terms!")
