# On a piano, a key has a frequency, say f0. Each higher key (black or white) has a frequency
#  of f0 * rn, where n is the distance (number of keys) from that key,
#  and r is 2(1/12). Given an initial key frequency, 
# 
# output that frequency and the next 3 higher key frequencies.

# Output each floating-point value with two digits after the decimal point, then the units ("Hz"), then a newline, using the following statement:
# print(f'{your_value:.2f} Hz')

# Ex: If the input is:

# 440
# (which is the A key near the middle of a piano keyboard), the output is:

# 440.00 Hz
# 466.16 Hz
# 493.88 Hz
# 523.25 Hz
# Note: To compute the next 3 higher key frequencies, use one statement to compute r = 2(1/12) using the pow function (remember to import the math module). Then use that r in subsequent statements that use the formula fn = f0 * rn with n being 1, 2, and finally 3.

import math
f0 = float(input())

r = math.pow(2, 1/12)
f1 = f0 * r
f2 = f0 * (r**2)
f3 = f0 * (r**3)        

print(f'{f0:.2f} Hz')
print(f'{f1:.2f} Hz')       
print(f'{f2:.2f} Hz')
print(f'{f3:.2f} Hz')
