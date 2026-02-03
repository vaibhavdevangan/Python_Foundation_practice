# Driving is expensive.
#  Write a program with a car's miles/gallon and gas dollars/gallon (both floats)
#   as input, and output the gas cost for 20 miles, 75 miles, and 500 miles.  
#   Output each floating-point value with two digits after the decimal point, 
#   which can be achieved as follows:
#    print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}') 
#     Ex: If the input is:  20.0 3.1599
#      Then the output is:  3.16 11.85 79.00

miles_per_gallon = float(input())
dollars_per_gallon = float(input())

gas_cost1= (20 / miles_per_gallon) * dollars_per_gallon
gas_cost2= (75 / miles_per_gallon) * dollars_per_gallon     
gas_cost3= (500 / miles_per_gallon) * dollars_per_gallon

print(f'{gas_cost1:.2f} {gas_cost2:.2f} {gas_cost3:.2f}')