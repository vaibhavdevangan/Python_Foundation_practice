# # Prompt the user to input an integer between 32 and 126, a float, a character, and a string,
#  storing each into separate variables. 
# Then, output those four values on a single line separated by a space.
#  (Submit for 2 points).

# Enter integer (32 - 126):
# 99
# Enter float:
# 3.77
# Enter character:
# z
# Enter string:
# Howdy
# 99 3.77 z Howdy

# (2) Extend to also output in reverse. (Submit for 1 point, so 3 points total).

# Enter integer (32 - 126):
# 99
# Enter float:
# 3.77
# Enter character:
# z
# Enter string:
# Howdy
# 99 3.77 z Howdy
# Howdy z 3.77 99

# (3) Extend to convert the integer to a character by using the 'chr()' function, and output that character. (Submit for 2 points, so 5 points total).

# Enter integer (32 - 126):
# 99
# Enter float:
# 3.77
# Enter character:
# z
# Enter string:
# Howdy
# 99 3.77 z Howdy
# Howdy z 3.77 99
# 99 converted to a character is c

user_int = int(input("Enter integer (32 - 126):\n"))    
user_float = float(input("Enter float:\n"))

user_char = input("Enter character:\n")
user_string = input("Enter string:\n")

print(f'{user_int} {user_float} {user_char} {user_string}')
print(f'{user_string} {user_char} {user_float} {user_int}')
print(f'{user_int} converted to a character is {chr(user_int)}')
