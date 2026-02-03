# Note: When accuracy is essential, floats are not used to represent currency 
#due to rounding and accumulation errors. Python provides several primitives 
# specifically developed to implement financial applications. However, these topics are beyond the scope of this lab.

# Output each floating-point value with two digits after the decimal point, 
# which can be achieved as follows:
# print(f'{your_value:.2f}')

# (1) Prompt the user to input a food item name, price, and quantity.
#  Output an itemized receipt. (Submit for 2 points)

# Enter food item name:
# hot dog
# Enter item price:
# 2.00
# Enter item quantity:
# 5

# RECEIPT
# 5 hot dog @ 
# 2.00
# =
# 2.00=10.00
# Total cost: $10.00

# (2) Extend the program to prompt the user for a second item. Output an itemized receipt. (Submit for 2 points, so 4 points total)

# Enter food item name:
# hot dog
# Enter item price:
# 2.00
# Enter item quantity:
# 5

# RECEIPT
# 5 hot dog @ 
# 2.00
# =
# 2.00=10.00
# Total cost: $10.00

# Enter second food item name:
# ice cream
# Enter item price:
# 2.50
# Enter item quantity:
# 4

# RECEIPT
# 5 hot dog @ 
# 2.00
# =
# 2.00=10.00
# 4 ice cream @ 
# 2.50
# =
# 2.50=10.00
# Total cost: $20.00

# (3) Extend again to output a third receipt that adds a mandatory 15% gratuity to the total cost. Output the total cost, the cost of gratuity, and the grand total. (Submit for 3 points, so 7 points total)

# Enter food item name:
# hot dog
# Enter item price:
# 2.00
# Enter item quantity:
# 5

# RECEIPT
# 5 hot dog @ 
# 2.00
# =
# 2.00=10.00
# Total cost: $10.00

# Enter second food item name:
# ice cream
# Enter item price:
# 2.50
# Enter item quantity:
# 4

# RECEIPT
# 5 hot dog @ 
# 2.00
# =
# 2.00=10.00
# 4 ice cream @ 
# 2.50
# =
# 2.50=10.00
# Total cost: $20.00

# 15% gratuity: $3.00

# Total with tip: $23.00