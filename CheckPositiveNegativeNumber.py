Num = float(input("What is the number you would like to check \n"))

if Num < 0 :
    print("The number {0} is a negative number".format(Num))
    
elif Num == 0 :
    print("The number 0 is neither a positive number or a negative number. It is the midpoint of the number line.")

else :
    print("The number {0} is a positive number".format(Num))
    
