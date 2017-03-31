# 
import pandas as pd
import numpy as np
import csv

# Kernal Density Estimate Function
def kde_setosa(h,slength,swidth,plength,pwidth):
    iris_setosa = pd.read_csv('iris.setosa')
    M_1 = len(iris_setosa)
    print('Number of training setosa',len(iris_setosa))

    kde = []
    for j in range(0,len(slength)):
        K_h_array = []
        for i in range(0,len(iris_setosa)):
            #print(i)
            x_xi = ((slength[j] - iris_setosa.sL[i])**2 + \
                    (swidth[j] - iris_setosa.sW[i])**2 +  \
                    (plength[j] - iris_setosa.pL[i])**2 + \
                    (pwidth[j] - iris_setosa.pW[i])**2)**(0.5)
        
            K_h    = (1/((2*np.pi)**(0.5)*h))**4 * np.exp(-(x_xi)**2 / (2*h**2))
            K_h_array.append(K_h)

        p_x_C1 = (1/M_1)*np.sum(K_h_array)
        kde.append(p_x_C1)
    df = pd.DataFrame(kde,columns=['KDE-setosa'])
    return df

def kde_versicolor(h,slength,swidth,plength,pwidth):
    iris_versicolor = pd.read_csv('iris.versicolor')
    M_1 = len(iris_versicolor)
    print('Number of training versicolor',len(iris_versicolor))

    kde = []
    for j in range(0,len(slength)):
        K_h_array = []
        for i in range(0,len(iris_versicolor)):
            #print(i)                                                                      
            x_xi = ((slength[j] - iris_versicolor.sL[i])**2 + \
                    (swidth[j] - iris_versicolor.sW[i])**2 +  \
                    (plength[j] - iris_versicolor.pL[i])**2 + \
                    (pwidth[j] - iris_versicolor.pW[i])**2)**(0.5)

            K_h    = (1/((2*np.pi)**(0.5)*h))**4 * np.exp(-(x_xi)**2 / (2*h**2))
            K_h_array.append(K_h)

        p_x_C1 = (1/M_1)*np.sum(K_h_array)
        kde.append(p_x_C1)
    df = pd.DataFrame(kde,columns=['KDE-versicolor'])
    return df

def kde_virginica(h,slength,swidth,plength,pwidth):
    iris_virginica = pd.read_csv('iris.virginica')
    M_1 = len(iris_virginica)
    print('Number of training virginica',len(iris_virginica))

    kde = []
    for j in range(0,len(slength)):
        K_h_array = []
        for i in range(0,len(iris_virginica)):
            #print(i)                                                                      
            x_xi = ((slength[j] - iris_virginica.sL[i])**2 + \
                    (swidth[j] - iris_virginica.sW[i])**2 +  \
                    (plength[j] - iris_virginica.pL[i])**2 + \
                    (pwidth[j] - iris_virginica.pW[i])**2)**(0.5)

            K_h    = (1/((2*np.pi)**(0.5)*h))**4 * np.exp(-(x_xi)**2 / (2*h**2))
            K_h_array.append(K_h)

        p_x_C1 = (1/M_1)*np.sum(K_h_array)
        kde.append(p_x_C1)
    df = pd.DataFrame(kde,columns=['KDE-virginica'])
    return df
