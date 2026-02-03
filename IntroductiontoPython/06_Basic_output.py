# A variable like user_num can store a value like an integer. Extend the 
# given program as indicated.

# Output the user's input. (2 pts)
# Output the input squared and cubed.
# Hint: Compute squared as "user_num*user_num." (2 pts)
# Get a second user input into user_num2, and output the sum and product. (1 pt)
# Sample Output
# '''
# Enter integer:
# 4
# You entered: 4
# 4 squared is 16
# And 4 cubed is 64 !!
# Enter another integer:
# 5
# 4 + 5 is 9
# 4 * 5 is 20

user_num = int(input("Enter integer:\n"))
print("You entered:", user_num)
squared = user_num * user_num
cubed = user_num * user_num * user_num
print(f"{user_num} squared is {squared}")
print(f"And {user_num} cubed is {cubed} !!")    

user_num2 = int(input("Enter another integer:\n"))
sum_result = user_num + user_num2
product_result = user_num * user_num2
print(f"{user_num} + {user_num2} is {sum_result}")
print(f"{user_num} * {user_num2} is {product_result}")  

