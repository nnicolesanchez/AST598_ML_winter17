# This script makes the data for problem set 3
#      N, number of pairs 
#      mu, mean 
#      sigma, standard deviation

# N. Nicole Sanchez      -- AST 598: Machine Learning
# Univ. of Wash, Seattle -- Problem Set 3  
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import numpy as np
import sys

if len(sys.argv) != 4:
    print(r'Please provide values for N, '+u'\u03BC'','+u' \u03C3')
    quit()
print(sys.argv)

N     = int(sys.argv[1])
mu    = float(sys.argv[2])
sigma = float(sys.argv[3])

x = np.random.normal(mu,sigma,N)
np.savetxt('data.out',x)
