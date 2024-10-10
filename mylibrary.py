import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# example of graph
# years=np.array([2020,2021,2022,2026])
# grade=([95,80,75,80])
# plt.plot(years,grade,marker="o")
# plt.title("My Academic Grades")
# plt.xlabel("years")
# plt.ylabel("grades")
# plt.grid()
# plt.show()


x=np.array([90,75,80,65])
plt.pie(x)
plt.title("Grades")

plt.show()