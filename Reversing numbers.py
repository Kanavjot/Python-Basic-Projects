num = int(input("Please enter the number you would like to be reversed: \n"))
reverse_number = 0

print("Given Number = {0}".format(num))

while num > 0:
    remainder = num % 10
    reverse_number = (reverse_number * 10)+ remainder
    num = num // 10
print("Reverse number = {0}".format(reverse_number))