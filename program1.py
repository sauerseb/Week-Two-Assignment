# __author__ = Evan Sauers (sauerseb)

# CIS-125-82A
# program1.py
#
# This program computes and prints a table of Celsius temperatures and the Fahrenheit equivalents every 10 degrees from 0C to 100C.

# C=Celsius
# F=Farenheit

# Print a table of results
# Convert to Celsius
# (F-32) * 5 / 9

def main(): 
    for C in range(0, 101, 10):
        F = (9/5 * C) +32
        print(C,F)

main()


# Results:
#0 32.0                                                                                                                                                                                  
#10 50.0                                                                                                                                                                                 
#20 68.0                                                                                                                                                                                 
#30 86.0                                                                                                                                                                                 
#40 104.0                                                                                                                                                                                
#50 122.0                                                                                                                                                                                
#60 140.0                                                                                                                                                                                
#70 158.0                                                                                                                                                                                
#80 176.0                                                                                                                                                                                
#90 194.0                                                                                                                                                                                
#100 212.0
