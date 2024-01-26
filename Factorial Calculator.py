Num = int(input("Please enter the Number: "))

F = 1

if Num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif Num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,Num + 1):
       F = F*i
   print("The factorial of {0} is {1}".format(Num , F))