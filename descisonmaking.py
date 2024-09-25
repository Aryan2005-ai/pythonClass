# check you are eligible for voting or not 
# get the age from user
age=int(input("enter your age"))
if age > 18 and age< 55:
    print("you are eligible for voting")
elif age> 55:
    print(" you are eligible for supervote")
else:
    print("you are not eligible for voting")

