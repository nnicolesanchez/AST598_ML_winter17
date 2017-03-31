#
#


#
#
import pandas as pd
import numpy as np



def nearest_neighbor(slength,swidth,plength,pwidth):
    iris_train = pd.read_csv('iris.train')

    distance = ((slength - iris_train.sL)**2 + \
                (swidth - iris_train.sW)**2 +  \
                (plength - iris_train.pL)**2 + \
                (pwidth - iris_train.pW)**2)**(0.5)
    return iris_train.Cl[np.argmin(distance)]


iris_test = pd.read_csv('iris.test')
print(iris_test.Cl)

text_file = open("nn.out", "w")
text_file.write("# nearest neighbor, true\n")

for i in range(0,len(iris_test)):
    value = nearest_neighbor(iris_test.sL[i],iris_test.sW[i],\
                             iris_test.pL[i],iris_test.pW[i])
    text_file.write(value+','+iris_test.Cl[i]+'\n')
    print(value)

text_file.close()
    


    



