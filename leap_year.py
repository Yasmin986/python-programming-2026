# Write a Python program to check whether the given year is leap year or not.

year = int(input("Enter a year : "))

if year % 4 == 0:
    print(year , " is a leap year.")
elif(year % 400 == 0):
    print(year , " is a leap year.")
elif(year % 100 == 0):
    print(year , " is not a leap year.")
else:
    print(year , " is not a leap year.")

# Time Complexity
# Time: O(1)
# Space: O(1)