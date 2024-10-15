import numpy as np
import pandas as pd
myData=np.arange(0,1000000)
# print(myData)
myframe=pd.DataFrame(data=myData.reshape(100000,10))
# print(myframe)
# print(myframe.head())
# print(myframe.loc[ [10,10] ])
# print(myframe.tail(1))
print(myframe.loc[ [2,] ])

