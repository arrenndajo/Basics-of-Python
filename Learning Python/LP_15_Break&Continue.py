# Break and Continue
students = ["ram", "shyam", "kishan", "radha", "radhika"]

# break
for student in students:
    if student == "radha":
        # here radha and elements ahead of radha won't be printed
        break; # used to end the loop
    print(student)

# continue
for student in students:
    if student == "kishan": 
        # here kishan won't be printed, everything else will be printed
        continue; # used to continue the loop & not print the item^^
    print(student)
