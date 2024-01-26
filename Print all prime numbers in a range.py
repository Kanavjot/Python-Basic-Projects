# Program to print all the prime number between 1 to 1000
num = int(input("Please enter the starting number:"))
num1 = int(input("Please enter the ending number:"))


factor = []
pn = []
for i in range(num,num1+1):
    for j in range (1,i+1):
        if (i%j==0):
            factor.append(j)
    if len(factor) == 2:
        
        pn.append(i) 
    factor=[] 
print("All the prime numbers between {0} to {1} are\n {2}".format(num,num1,pn))   
    