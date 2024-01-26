print("What would you like to calculate?")
C = int(input("1- Compound Interest\n2- Simple Interest"))
P = float(input("Principal="))
R = float(input("Rate Of Interest="))
T = float(input("Time in Years="))

SI = (P * T * R / 100)
SIA = P + SI

CI = (P * (1 + R / 100) ** T) - P
CIA = P + CI

if C == 1:
    print("The Compound Interest formed on the principal of {0} at a {1} percent rate of interest in a time of {2} years is {3}. The Total amount is {4}.".format(P, R, T, CI, CIA))
else:
    print("The Simple Interest formed on the principal of {0} at a {1} percent rate of interest in a time of {2} years is {3}. The Total amount is {4}.".format(P, R, T, SI, SIA))


    

