# Tuple is same as List but its immutable
# You can append/clear a List 
# You cannot edit/change/delete a Tuple

marks = (95, 98, 97, 97, 97)

# marks[0] = 99 # This cannot be done! You cannot change a Tuple.

print(marks.count(97)) # prints the count of a particular number
print(marks.index(97)) # prints the index of a particular number
# prints only the index of the same number appeared for the 1st time in the tuple




for i in range(1,16):
    if (i<=10 and i%5==0):
        print("Buzz")
    elif (i<=12 and i%3==0):
        print("Fizz")
    elif (i>10 and i%5==0):
        print("FizzBuzz")
    else:
        print(i)
