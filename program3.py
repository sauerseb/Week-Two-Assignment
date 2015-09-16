# __author__ = Evan Sauers (sauerseb)

# CIS-125-82A
# program3.py
#
# This program prompts the user for a distance measured in kilometers, converts it to miles, and prints out the results. 

# K= kilometers
# M= miles

# Ask user for a distance in kilometers
# Convert to miles
# (K * .62)

K = eval(input("Please enter a distance in kilometers: "))

M = (K * .621371192)

print("The distance" , K, " in kilometers is equal to " , M, "miles")
