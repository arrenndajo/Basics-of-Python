age = input("What is your age? ")
print(age)
age = int(age)

if age >= 18:
    print("You are an adult")
    print("You can vote")
elif age < 18 and age > 3:
    print("You are in school")
else:
    print("You are a child")