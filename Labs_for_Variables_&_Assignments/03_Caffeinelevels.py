# A half-life is the amount of time it takes for a substance or entity to fall to
#  half its original value. Caffeine has a half-life of about 6 hours in humans. 
# Given caffeine amount (in mg) as input, output the caffeine level after 6, 12, and 24 hours.
#  Use a string formatting expression with conversion specifiers to output the caffeine amount as floating-point numbers.

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print(f'{your_value:.2f}')
# Ex: If the input is:

# 100

# the output is:

# After 6 hours: 50.00 mg
# After 12 hours: 25.00 mg
# After 24 hours: 6.25 mg
# Note: A cup of coffee has about 100 mg. A soda has about 40 mg. An "energy" drink (a misnomer) has between 100 mg and 200 mg.


caff_amt_mg = int(input("caff_amt_mg: "))
# time_duration = int(input("time_durationn: "))


caff_level1 = caff_amt_mg/2
caff_level2 = caff_level1/2
caff_level3 = caff_level2/4

print("After 6 hours",f'{caff_level1:.2f}')
print("After 12 hours:",f'{caff_level2:.3f}')
print("After 24 hours:",f'{caff_level3:.2f}' )

