# Written by Thy H. Nguyen

thy = input ("Enter the first number: ")
thuy = input("Enter the second number: ")
thuyy = input("Enter the third number:  ")
ans = input("finite or infinite")
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

        if ans == "finite" and x!= 1:
            print("The sum of this finite geometric series is: ", ((value_1)*(1-x**3))/(1-x))


        if ans == "infinite":
            print("b")

        if ans != "finite" and ans != "infinite":
            print('Please choose one, and only enter "finite" or "infinite!"')

    except ValueError:
        print("Please enter the value again. DO NOT ENTER FRACTIONS!!! DO NOT ENTER WORDS!!!")

except ZeroDivisionError:
    print("cannot devide 0")
