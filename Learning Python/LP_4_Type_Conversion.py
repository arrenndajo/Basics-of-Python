# Type Conversion

# We get the input from the user in the form of String

# We can concatenate str to str, not str to int.
# Type of valid values can be converted into string, integer, float, boolean
# str(), int(), float(), bool()

old_age = input("Enter your old age: ")
# new_age = old_age + 2, here old_age is taken as string

new_age = int(old_age) + 2
print(new_age)

# Example 
number = 18
print(type(number))
print(float(number))

# Print sum of 2 numbers

first = input("Enter first number: ")
second = input("Enter second number: ")

sum = int(first) + int(second)
print("The sum is " + str(sum))