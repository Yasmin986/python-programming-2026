# Write a Python program to print first n Fibonacci numbers.
# What is the Fibonacci Series?

# Each number is the sum of the previous two numbers.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
a = 0
b = 1
n = int(input("Enter n : "))

for i in range(n):
    print(a, end=" ")
    next = a + b
    a = b
    b = next
