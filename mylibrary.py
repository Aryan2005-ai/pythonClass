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


# x=np.array([90,75,80,65])
# plt.pie(x)
# plt.title("Grades")
# name=["python","java","react","c"]
# plt.legend(name)
# plt.pie(x, labels = name)
# plt.show()



# years = [2019, 2020, 2021, 2022, 2023]
# grades = [85, 88, 90, 87, 92]

# plt.bar(years, grades, color='red')
# plt.xlabel('Years')
# plt.ylabel('Grades')
# plt.title('Grades Over Years')
# plt.show()



years = [2019, 2020, 2021, 2022, 2023]
grades = [85, 88, 90, 87, 92]

plt.scatter(years, grades, color='red')
plt.xlabel('Years')
plt.ylabel('Grades')
plt.title('Grades Over Years')
plt.show()