import random
otp=random.randint(100000,900000)
print('otp',otp)


#to convert usd to indian currency.

dollar=int(input("enter your currency value in dollar"))
rupee=dollar*84
print("the value of usd is",rupee,"rupees")

#to convert indian currency to usd 

rupee=int(input("enter your currency value in IND"))
USD=rupee/84
print("the value of usd is",USD,"dollar")
