# This script creates a plot of petal length vs. petal width for 
# the three types of Irises from HW 4
import matplotlib.pyplot as plt
import pandas as pd

iris_setosa     = pd.read_csv('iris.setosa')
iris_virginica = pd.read_csv('iris.virginica')
iris_versicolor =pd.read_csv('iris.versicolor')

fig = plt.figure(figsize=(6, 4))
ax1 = fig.add_subplot(111)
#ax2 = fig.add_subplot(312)
#ax3 = fig.add_subplot(313)

ax1.plot(iris_setosa.pL,iris_setosa.pW,'.',color='Salmon',label='Setosa')
ax1.plot(iris_virginica.pL,iris_virginica.pW,'.',color='SteelBlue',label='Virginica')
ax1.plot(iris_versicolor.pL,iris_versicolor.pW,'.',color='MediumPurple',label='Versicolor')
ax1.set_ylabel('Petal Width')
ax1.set_xlabel('Petal Length')
ax1.legend()
plt.savefig('iris_petal_plot.ps')
plt.show()
