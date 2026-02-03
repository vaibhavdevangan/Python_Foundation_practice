# Auto-graded programming assignments have numerous advantages, but have some 
# challenges too. Students commonly struggle with realizing that example input / output 
# provided in an assignment's specification interleaves input and output, but the program
#  should only output the output parts. If a program should double its input, an instructor
#   might provide this example:

# Enter x:
# 5
# x doubled is: 10


x = int(input("Enter a number:"))
print("x doubled is:", 2 * x)


# The student might copy the entire example as their program, leading to incorrect output.
# To help students understand this concept, we can provide a simple exercise where they
#  must write a program that reads an integer and outputs its double, without any extra prompts
#   or text.
