import kde_functions as kde
import pandas as pd
import numpy as np
import csv
import sys

if len(sys.argv) != 2:
    print(r'Please provide value for bandwidth, h')
    quit()

h = float(sys.argv[1]) 

iris_test = pd.read_csv('iris.test')
print(len(iris_test))

slength = iris_test.sL
swidth  = iris_test.sW
plength = iris_test.pL
pwidth  = iris_test.pW

kde_setosa     = kde.kde_setosa(h,slength,swidth,plength,pwidth) 
kde_versicolor = kde.kde_versicolor(h,slength,swidth,plength,pwidth)
kde_virginica  = kde.kde_virginica(h,slength,swidth,plength,pwidth)

kde_df = pd.concat([kde_setosa, kde_versicolor, kde_virginica, iris_test.Cl], axis=1)
print(kde_df)

kde_df.to_csv('kde.out',index=False)
