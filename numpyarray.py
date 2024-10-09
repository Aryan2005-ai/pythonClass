import numpy as np

#assign array in numpy

# myData=np.array([1,2,3,4])
# print(myData)
# print(type(myData))

#update the data in array
# myData[0]=9
# print(myData)

# myData[0]=9
# myData[1]=10
# myData[2]=11
# myData[3]=12
# print(myData)

# using for loop
# y=12
# for x in range(0,4):
#     myData[x]=y
#     y=y-1
# print(myData)


# using while loop
# x=0
# y=12


# while x<4:
#     myData[x]=y
#     y=y-1
#     x=x+1
# print(myData)

# myData=np.array([1,2,3,4])

# myfriends=np.array(["aryan","anshul","wani","anjali"])
# for name in myfriends:
#     print(name)
#     rev=np.flip(myfriends)
# print(rev)

# myfriends=np.array(["aryan","anshul","wani","anjali"])
# for x in range(4,0):
#         rev=myfriends[x]
#         x=x-1
#         print(rev)

myfriends=np.array(["aryan","chris","wani","bhumi"])
for name in myfriends:
    s=np.sort(myfriends)
print(s)

