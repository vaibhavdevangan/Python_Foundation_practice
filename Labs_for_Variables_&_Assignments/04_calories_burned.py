# The following equation estimates the average calories burned for a person 
# when exercising, which is based on a scientific journal article (source):https://www.tandfonline.com/doi/abs/10.1080/02640410470001730089

# Calories = ( (Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991 ) x Time / 8.368

# Write a program using inputs age (years), weight (pounds), heart rate (beats per minute), and time (minutes), respectively.
#  Output the average calories burned for a person.

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print(f'Calories: {calories:.2f} calories')

# Ex: If the input is:

# 49
# 155
# 148
# 60
# then the output is:

# Calories: 736.21 calories


age_years = int(input(": "))
weight_pounds = int(input(": "))
heart_rate_bit_per_min = int(input(": "))
time_minutes = int(input(": "))

Calories = ( ( age_years * 0.2757) + ( weight_pounds * 0.03295 ) + (heart_rate_bit_per_min * 1.0781) - 75.4991 ) * time_minutes / 8.368

print(f'Calories :{Calories:.2f}') 
