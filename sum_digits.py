sum = 0
num = int(input("Enter a number : "))
while (num >0):
    lastDigit = num%10
    sum += lastDigit
    num = num //10

print("Sum of digits = ", sum)



    
     

