# K-fold cross validation method with k = 5 folds
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold

# from nicolesanchez_hw1: python fitdata.py data.out
# model: y = ax * b
#a = 1.1
#b = 1.88
k = 5

def get_b(y,x,y_mean,x_mean):
    b_1 = (np.average(x*y) - (x_mean*y_mean))/(np.average(x**2.) - (x_mean**2.))
    return b_1

def get_a(y,x,b_1,y_mean,x_mean):
    b_0 = y_mean - (b_1*x_mean)
    return b_0

def get_a_b(x,y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    b = get_b(y,x,y_mean,x_mean)
    a = get_a(y,x,b,y_mean,x_mean)
    #print(a,b)
    return a,b


df = pd.read_csv('data.out',names=['x','y'],sep=' ')
N  = len(df)
n = int(N/k)

kernal1 = np.linspace(0,(N/5)-1,n,dtype=int)
kernal2 = np.linspace((N/5),(2*N/5)-1,n,dtype=int)
kernal3 = np.linspace((2*N/5),(3*N/5)-1,n,dtype=int)
kernal4 = np.linspace((3*N/5),(4*N/5)-1,n,dtype=int)
kernal5 = np.linspace((4*N/5),N-1,n,dtype=int)
kernals = [kernal1,kernal2,kernal3,kernal4,kernal5]

mse_avg = []
for i in range(len(kernals)):
    print('Test set is kernal '+str(i))
    df_test     = kernals[i]
    df_test_x = df.x[df_test]
    df_test_y = df.y[df_test]
    #print(df_test_x)

    a,b = get_a_b(df_test_x,df_test_y)
    #print(a,b)

    df_train  = df.drop(df_test_x.index)
    #print(df_training)
    
    model_y = a*df_train.x + b
    mse     = np.abs((df_train.y - model_y))
    mse_mn  = np.mean(mse) 
    mse_avg.append(mse_mn)
    print('MSE is',round(mse_mn,4))

print('Average MSE over all training sets is: ',round(np.average(mse_avg),4))

text_file = open("crossvalidate5.out", "w")
text_file.write("# Average MSE \n")
text_file.write(str(round(np.average(mse_avg),4))+'\n')
