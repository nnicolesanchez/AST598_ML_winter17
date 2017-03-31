# This script writes out iris.train with 140 lines
# and iris.test with 10 lines from the original
# iris.data file with 150 lines
import numpy as np
import pandas as pd

# Define DataFrame
iris = pd.read_csv('iris.data',names=['sL','sW','pL','pW','Cl'])

iris_test  = iris.sample(10)
iris_train = iris.drop(iris_test.index)

iris_train.to_csv('iris.train',index=False)
iris_test.to_csv('iris.test',index=False)
