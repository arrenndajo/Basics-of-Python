# Sets is used when we don't want to keep duplicates of the items present in the Tuple

# [] means List
# () means Tuple
# {} means Set

marks = {95, 98, 97, 97, 97}
print(marks) # only unique value gets printed. no duplicate values

# since index is not present here. Sets is unordered sequence of elements

for score in marks:
    print(score) 
    
age = {19, 45, 23, 67, 67, 45}
print(age)