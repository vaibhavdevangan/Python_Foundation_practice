# Output each floating-point value with two digits after the decimal point, 
# which can be achieved as follows:
# print(f'{your_value:.2f}')

# (1) Prompt the user to input a wall's height and width. Calculate and'
# ' output the wall's area (integer). (Submit for 2 points).

# Enter wall height (feet):
# 12
# Enter wall width (feet):
# 15
# Wall area: 180 square feet

# (2) Extend to also calculate and output the amount of paint in gallons needed to paint the wall (floating point). Assume a gallon of paint covers 350 square feet. Store this value in a variable. Output the amount of paint needed using the %f conversion specifier. (Submit for 2 points, so 4 points total).

# Enter wall height (feet):
# 12
# Enter wall width (feet):
# 15
# Wall area: 180 square feet
# Paint needed: 0.51 gallons

# (3) Extend to also calculate and output the number of 1 gallon cans needed to paint the wall. Hint: Use a math function to round up to the nearest gallon. (Submit for 2 points, so 6 points total).

# Enter wall height (feet):
# 12
# Enter wall width (feet):
# 15
# Wall area: 180 square feet
# Paint needed: 0.51 gallons
# Cans needed: 1 can(s)

# (4) Extend by prompting the user for a color they want to paint the walls.
#  Calculate and output the total cost of the paint cans depending on which color is chosen.
#  Hint: Use a dictionary to associate each paint color with its respective cost. 
# Red paint costs 
# 35
# p
# e
# r
# g
# a
# l
# l
# o
# n
# c
# a
# n
# ,
# b
# l
# u
# e
# p
# a
# i
# n
# t
# c
# o
# s
# t
# s
# 35pergalloncan,bluepaintcosts25 per gallon can, and green paint costs $23 per gallon can. (Submit for 2 points, so 8 points total).

# Enter wall height (feet):
# 12
# Enter wall width (feet):
# 15
# Wall area: 180 square feet
# Paint needed: 0.51 gallons
# Cans needed: 1 can(s)

wall_height = float(input('Enter wall height (feet):\n'))   
wall_width = float(input('Enter wall width (feet):\n'))

wall_area = wall_height * wall_width
print(f'Wall area: {int(wall_area)} square feet')

paint_needed = wall_area / 350
print(f'Paint needed: {paint_needed:.2f} gallons')

