# Written by Thy H. Nguyen

thy = input ("Enter the first number: ")
thuy = input("Enter the second number: ")
thuyy = input("Enter the third number:  ")
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

        ans = input("Choose finite or infinite: ")
        if ans == "finite":
            print ("The finite geometric series is", thy, "+", thuy, "+", thuyy)
            if x<1 or x>1:
                print ("The sum of the finite geometric series is", ((value_1)*(1-x**3))/(1-x))
            if x ==1 :
                print ("The sum of the finite geometric series is", value_1 + value_2 + value_3)
        if ans == "infinite" and abs(x) <1 :
                print ("The infinite geometric series is", thy, "+", thuy, "+", thuyy, "+ ...")
                print ("The sum of the infinite geometric series is", ((value_1)/(1-x))
        else:
                print ("The sum of the infinite geometric series diverges.")

    else:
        print("This is not a geometric series!!!")

except ValueError:
    print("Please enter the value again. DO NOT ENTER FRACTIONS!!! DO NOT ENTER WORDS!!!")
