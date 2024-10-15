import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics
# x=np.array([1,7,8,11,9,3,2,4])
# mean=x.mean()
# maximum=x.max()
# minimum=x.min()
# print(mean)
# print(maximum)
# print(minimum)
# median=statistics.median(x)
# mode=statistics.mode(x)
# print(median)
# print(mode)
# x.sort()
# print(x)

# for i in x:
#     print(i)

# print(x[0:7])
# print(x[-6:-2])
# print(x.shape)


# mydata=x.reshape(2,4)
# print(mydata)

# y=np.array([3,1,7,9,2,11,8,10])

# z=x+y

# print(z)


# x=np.array([1,2,3,4])
# mydataframe=pd.DataFrame(x)
# print(mydataframe)

mydata=pd.DataFrame(data=np.arange(0,100).reshape(10,10))
# print(mydata+1000)
# print(mydata.describe())
# a=mydata.mean()
# b=mydata.median()
# c=mydata.mode()
# print(a)
# print(b)
# print(c)
print(mydata.loc[ [ 0,] ])

# print(mydata.head())
# print(mydata.tail())
# print(mydata.head(7))