Num=int(input("Please enter your number: "))

F=[]

for i in range(1,Num+1):
    if Num % i == 0:
        F.append(i)
        
NF=len(F)

if Num <= 0:
    print("Negative numbers and 0 are not prime nor composite.")
    exit

elif Num == 1 :
    print("The Number 1 is not a prime number or a composite number.\nIt has exactly one factor which is the number 1 itself.\nHence it is called a unique number")
    exit 
    
elif Num >= 2:
     if NF == 2 :
         print("The Number {0} is a prime number.".format(Num))
         print("Its Factors are {0}".format(F))
     else:
        print("The Number {0} is a composite number.".format(Num))
        print("Its Factors are {0}".format(F))