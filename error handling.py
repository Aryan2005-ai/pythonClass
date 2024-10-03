# error handling
# try:
    # error
# catch:
#     type of error

# print(x)

# NameError
try:
    print(y)
except NameError:
    print("y not defined")
# ZeroDivisionError
try:
    y=1/0
    print(y)
except ZeroDivisionError:
    print("zero division error")
# ValueError
try:
    y="aryan"
    b=int(y)
    print(y)
except ValueError:
    print("string will not cast in int")

# FileNotFoundError
try:
    import os
    os.remove("myfile.txt")
except FileNotFoundError:
    print("file not found")


# IndexError
mylist=["pawan","aryan","ayush"]
try:
    print(mylist[4])
except IndexError:
    print("index out of range")



x=5
if x>5:
    print(x)
else:
    print(x)

# type error
x="aryan"
y=4
try:
    c=x+y
    print(c)
except TypeError:
    print("type error")
finally:
    print("always run")