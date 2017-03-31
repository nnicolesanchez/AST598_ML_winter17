# This script creates a parallel coordinate plot for 
# the three types of Irises from HW 4

from pandas.tools.plotting import parallel_coordinates
import matplotlib.pyplot as plt
import pandas as pd

iris_setosa     = pd.read_csv('iris.setosa')
iris_virginica = pd.read_csv('iris.virginica')
iris_versicolor =pd.read_csv('iris.versicolor')

plt.figure()
parallel_coordinates(iris_setosa,'Cl',color='Salmon')
parallel_coordinates(iris_virginica,'Cl',color='SteelBlue')
parallel_coordinates(iris_versicolor,'Cl',color='MediumPurple')
plt.savefig('iris_parallel_coor.ps')
plt.show()
