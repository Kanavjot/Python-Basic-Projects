Num1=int(input("Enter the First Number:"))
Num2=int(input("Enter the Second Number:"))
F1 = []
F2 = []
CF = []

if Num1 > Num2:
    S = Num2
    
else:
    S = Num1
    
for j in range (1,Num1+1):
    if Num1 % j == 0:
        F1.append(j)  
        
        
for l in range (1,Num2+1):
    if Num2 % l == 0:
        F2.append(l) 
       
    
for i in range (1,S+1):
    if(Num1 % i == 0) and (Num2 % i == 0):
        CF.append(i)
        
HCF = CF[-1]

LCM = (Num1 * Num2) / HCF



print ("The Factors of {0} are {1}.".format(Num1 , F1))
print ("The Factors of {0} are {1}.".format(Num2 , F2))
print ("The Common Factors of {0} and {1} are {2}.".format(Num1 , Num2 , CF))
print ("The Highest Common Factor of {0} and {1} is {2}.Their Lowest Common Multiple is {3}.".format(Num1 , Num2 , HCF , LCM))

