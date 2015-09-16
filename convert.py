# __author__ = Evan Sauers (sauerseb)

# CIS-125-82A
# convert.py
#
# This program computes and prints a table of Celsius temperatures and the Fahrenheit equivalents every 10 degrees from 0C to 100C.

# C=Celsius
# F=Farenheit

# Ask user for a temp in Fahrenheit
# Convert to Celsius
# (F-32) * 5 / 9

F = eval(input("Please enter a temp in Fahrenheit: "))

C = (F-32) * 5 / 9

print("The temp" , F, " in Fahrenheit is equal to " , C, "Celsius")

