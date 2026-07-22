# Write a Python program to check the given number is prime number or not.

num = int(input("Enter a num : "))

if num < 2:
    print("Not a Prime number")
else:
    isPrime = True

    for i in range(2, num):
        if num % 2 == 0:
            isPrime = False
            break

if isPrime:
    print("Prime number")
else:
    print("Not a Prime number")
