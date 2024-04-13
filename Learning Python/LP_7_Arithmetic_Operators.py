# Arithmetic Operators

print(5 + 2) # Addition
print(5 - 2) # Subtraction
print(5 * 2) # Multiplcation
print(5 / 2) # Division
print(5 // 2) # This is Division but w/o decimal
print(5 % 2) # Modulo, We get the Remainder as the answer
print(5 ** 2) # 5 to the power 2

# Shortcuts in Python
i = 5

i = 1 + 2
i += 2
# Both the lines above have the same meaning, gives the same answer
# Similarly, here are more shortcuts:
i -= 2
i *= 2
i /= 2

# Operator Precedence
result = 2 + 3 * 5 # Ans is 17 because of BODMAS rule
print(result)

# Example of Comments:

# Taking input
first = input("Enter first number: ")
second = input("Enter second number: ")

# Calculate sum
print(int(first) + int(second))