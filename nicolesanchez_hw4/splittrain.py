# This script

import pandas as pd

iris_train = pd.read_csv('iris.train')

iris_setosa     = iris_train[iris_train.Cl == ('Iris-setosa')]
iris_versicolor = iris_train[iris_train.Cl == ('Iris-versicolor')]
iris_virginica  = iris_train[iris_train.Cl == ('Iris-virginica')]

iris_setosa.to_csv('iris.setosa',index=False)
iris_versicolor.to_csv('iris.versicolor',index=False)
iris_virginica.to_csv('iris.virginica',index=False)
