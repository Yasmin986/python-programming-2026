# Write a Python program to find and display the maximum of three given numbers.

a = int(input("Enter first number: "))
print(a)
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if(a >= b):
    if(a >= c):
        max = a
    else:
        max = c
else:
    if (b >= c):
        max =b
    else:
        max =c

print ("Maximum of 3 numbers : ", max)            
