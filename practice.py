import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics
x=np.array([1,7,8,11,9,3,2])
mean=x.mean()
maximum=x.max()
minimum=x.min()
print(mean)
print(maximum)
print(minimum)
median=statistics.median(x)
mode=statistics.mode(x)
print(median)
print(mode)
x.sort()
print(x)

for i in x:
    print(i)