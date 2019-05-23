# North Seattle College, CSC 110
# Week 1 Lab
# Author: Zak Brinlee
# Email: zbrinlee@gmail.com

# Constants:
OUNCES_PER_POUND = 16

# User input:
ounces = float(input("Please enter the number of ounces: "))
fahrenheit = float(input("Please enter the degrees of Fahrenheit: "))

# Calculations:
pounds = (1 / OUNCES_PER_POUND) * ounces
celsius = 5/9 * (fahrenheit - 32)

# Output:
print(ounces, "oz is", pounds, "lbs")
print(fahrenheit, "degrees Fahrenheit is", celsius, "degrees in Celsius")