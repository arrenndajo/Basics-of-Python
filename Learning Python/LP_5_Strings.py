# Strings

# we can make changes to a string

name = "Jay Parmar"

print(name)
print(name.upper()) # Upper case text
print(name.lower()) # Lower case text

# Substring is a smaller part of the String

# Use single quotes '' for letters or characters and use double quotes "" for sentence or a paragraph

print(name.find('P')) 

# Here, P is at the 4th position. The index or position starts from 0
# 0,1,2,3,4 and so on

print(name.find('s'))

# -1 is printed in the output cuz 's' doesn't exist in the string^^

# We can replace a part of the string or the whole string:

print(name.replace("Parmar", "Superman"))

# We can also replace characters in the string:
print(name.replace('J', 'M'))