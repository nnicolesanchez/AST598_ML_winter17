import pandas as pd
import numpy as np
import sys

k_nearest = 3

iris_train = pd.read_csv('iris.train')
def nearest_neighbor3(slength,swidth,plength,pwidth):
    distance = ((slength - iris_train.sL)**2 + \
                    (swidth - iris_train.sW)**2 +  \
                    (plength - iris_train.pL)**2 + \
                    (pwidth - iris_train.pW)**2)**(0.5)
 
    return np.min(distance),distance#iris_train.Cl[np.sort(distance)]

iris_test = pd.read_csv('iris.test')

text_file = open("nn"+str(k_nearest)+".out", "w")
text_file.write("# nearest neighbor 1, 2, 3, true\n")

for i in range(0,len(iris_test)):
    value,distance = nearest_neighbor3(iris_test.sL[i],iris_test.sW[i],\
                             iris_test.pL[i],iris_test.pW[i])
    
    iris_train['d'+str(i)] = distance

    sorted = iris_train.sort_values('d'+str(i))
    sortCl = sorted.Cl.reset_index(drop=True)
    text_file.write(sortCl[0]+','+sortCl[1]+','+sortCl[2]+','+iris_test.Cl[i]+'\n')
