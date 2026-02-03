# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print(f'{your_value:.2f}')

# (1) Prompt the user for the number of cups of lemon juice, water, and agave nectar needed to make lemonade. Prompt the user to specify the number of servings the recipe yields. Output the ingredients and serving size. (Submit for 2 points).

# Note: This zyLab outputs a newline after each user-input prompt. For convenience in the examples below, the user's input value is shown on the next line, but such values don't actually appear as output when the program runs.

# Enter amount of lemon juice (in cups):
# 2
# Enter amount of water (in cups):
# 16
# Enter amount of agave nectar (in cups):
# 2.5
# How many servings does this make?
# 6

# Lemonade ingredients - yields 6.00 servings
# 2.00 cup(s) lemon juice
# 16.00 cup(s) water
# 2.50 cup(s) agave nectar

# (2) Prompt the user to specify the desired number of servings. Adjust the amounts of each ingredient accordingly, and then output the ingredients and serving size. (Submit for 4 points, so 6 points total).

# How many servings would you like to make?
# 48

# Lemonade ingredients - yields 48.00 servings
# 16.00 cup(s) lemon juice
# 128.00 cup(s) water
# 20.00 cup(s) agave nectar

# (3) Convert the ingredient measurements from (2) to gallons. Output the ingredients and serving size. Note: There are 16 cups in a gallon. (Submit for 2 points, so 8 points total).

# Lemonade ingredients - yields 48.00 servings
# 1.00 gallon(s) lemon juice
# 8.00 gallon(s) water
# 1.25 gallon(s) agave nectar


cups_lemon_juice = float(input("Enter amount of lemon juice (in cups):\n"))
cups_water = float(input("Enter amount of water (in cups):\n"))
cups_agave_nectar = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n"))


print(f'Lemonade ingredients - yields {servings:.2f} servings')
print(f'{cups_lemon_juice:.2f} cup(s) lemon juice')
print(f'{cups_water:.2f} cup(s) water')    
print(f'{cups_agave_nectar:.2f} cup(s) agave nectar')

desired_servings = float(input("How many servings would you like to make?\n"))
factor = desired_servings / servings
adjusted_lemon_juice = cups_lemon_juice * factor
adjusted_water = cups_water * factor
adjusted_agave_nectar = cups_agave_nectar * factor

print(f'Lemonade ingredients - yields {desired_servings:.2f} servings')
print(f'{adjusted_lemon_juice:.2f} cup(s) lemon juice')


print(f'{adjusted_water:.2f} cup(s) water')


print(f'{adjusted_agave_nectar:.2f} cup(s) agave nectar')

gallons_lemon_juice = adjusted_lemon_juice / 16
gallons_water = adjusted_water / 16
gallons_agave_nectar = adjusted_agave_nectar / 16
print(f'Lemonade ingredients - yields {desired_servings:.2f} servings')
print(f'{gallons_lemon_juice:.2f} gallon(s) lemon juice')
print(f'{gallons_water:.2f} gallon(s) water')
print(f'{gallons_agave_nectar:.2f} gallon(s) agave nectar')
