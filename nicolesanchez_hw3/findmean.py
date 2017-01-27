# This script finds the mean for data.out
#      data.out = [x_1, x_2, ..., x_N]

# N. Nicole Sanchez      -- AST 598: Machine Learning
# Univ. of Wash, Seattle -- Problem Set 3  
import matplotlib.pyplot as plt
import numpy as np
import sys

x = np.loadtxt('data.out')

x_mean = np.mean(x)
print('The mean of our x values: ',x_mean)
