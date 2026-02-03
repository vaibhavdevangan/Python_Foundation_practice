# Sites like Zillow get input about house prices from a database and provide nice summaries 
# for readers. 
# 
# Write a program with two inputs, current price and last month's price
#  (both integers). Then, output a summary listing the price, the change since last m
# onth, and the estimated monthly mortgage computed as (current_price * 0.051) / 12.

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print(f'{your_value:.2f}')
# Ex: If the input is:

# 200000
# 210000
# the output is:

# This house is 
# 200000.
# T
# h
# e
# c
# h
# a
# n
# g
# e
# i
# s
# 200000.Thechangeis-10000 since last month.
# The estimated monthly mortgage is $850.00.

current_price = int(input())
last_month_price = int(input())

change = current_price - last_month_price

estimated_mortgage = (current_price * 0.051) / 12

print(f'This house is \n{current_price}.')
print(f'The change is {change} since last month.')
print(f'The estimated monthly mortgage is ${estimated_mortgage:.2f}.')