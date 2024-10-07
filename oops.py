# OOPS in python
# objects based programming
# class,object,inheritance,polymorphism

# Syntax:

# class Aryan:
#     print("my name is aryan")
#     print("my age is **")

# class Details:
#     age=19
#     email="aryanoberoi2022@gmail.com"

# # object:Class=Class() syntax of object creation.
# aryan:Details=Details()
# print(aryan.age)
# print(aryan.email)

# class student:
#     def findMyAge(this,x,y):
#         # x=int(input("enter the value of current year"))
#         # y=int(input("enter the value of birth year"))
#         ageinyear=x-y
#         print(ageinyear)
# age:student=student()
# age.findMyAge(2024,2005)

# class student:
#     def findMyAge(this):
#         x=int(input("enter the value of current year"))
#         y=int(input("enter the value of birth year"))
#         ageinyear=x-y
#         print(ageinyear)
# age:student=student()
# age.findMyAge()

# class student:
#     def monthlyPocketMoney(this):
#         x=int(input("enter the amount of weekly income"))
#         moneyinmonth=x*4
#         print(moneyinmonth)
# money:student=student()
# money.monthlyPocketMoney()

class Car:
    model=2024
    Gears=7
    def speedmeasure(this):
      print("enter the values ranging from 1 to 7")
      x=int(input("enter the value of gear")) 
      speed=x*50
      print("top speed",speed)
aryan:Car=Car()
aryan.speedmeasure()



