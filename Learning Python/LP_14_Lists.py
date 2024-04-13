# Lists in Python

marks = [95, 98, 97] # this gets printed as it is
print(marks) 

marks = [95, 98, 97, "maths"] # this gets printed as it is
print(marks) 

marks = [95, 98, 97]
print(marks[0]) # number at the 0th index gets printed, here its 95

marks = [95, 98, 97] 
print(marks[-1]) # -1 is 97, -2 is 98 and so on
# the counting starts the last element and from -1

marks = [95, 98, 97]
print(marks[0:2]) # in 0:2, 0 and 1 is included, 2 is not included

marks = [95, 98, 97]
for score in marks:
    print(score)

# For loop in Lists
# Append Operation
# here the element gets inserted in the end
marks = [95, 98, 97]
marks.append(99)
print(marks)

# Insert Operation
# here the element gets printed at a particular index
marks = [95, 98, 97]
marks.insert(2, 99)
print(marks)

# True or False
print(99 in marks) # prints True if the element is present in the list
print(93 in marks) # prints False if the element isn't present in the list

print(len(marks)) # prints the length of the list, here it is 4^^^^

# While loop in lists
marks = [95, 98, 97]
i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

# Clear the list
marks.clear() # this will clear the list
print(marks)