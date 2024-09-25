#function can performs any task and it can reuse anytime

# def printname():
#     print("My function name is print")
# printname()


# def area():
#     x=int(input("enter the value of side"))
#     print("area of a square",x*x)
# area()

# def area():
#     x=int(input("enter the value of side"))
#     return x*x
# output=area()
# print("the area is",output)

def price():
    x=int(input("enter the delivery price of the product"))
    y=int(input("enter the price of the product"))
    z=int(input("enter the vat of the product"))
    a=int(input("enter the discount of the product"))
    return x+y+z-a
output=price()
print("the area is",output)