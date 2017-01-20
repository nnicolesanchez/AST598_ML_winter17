# The following parameters are required:
#      N, number of pairs of points
#      L, (-L,+L) values between which x is generated
#      beta_0, input parameter for likelihood
#      beta_1, input parameter for likelihood

# This script runs the functions in makedata.py
#  - It creates and saves a plot of binomial y(x) vs x
#  - It starts with input beta_0 and beta_1 and
#    iterates through 100x100 grid to optimize 
#    the beta parameters and maximize L(beta_0,beta_1)*
#  * Not to be confused with input param: L 


# N. Nicole Sanchez      -- AST 598: Machine Learning
# Univ. of Wash, Seattle -- Problem Set 2
import makedata as md
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import numpy as np
import sys

# Require input parameters
if len(sys.argv) != 5:
    print(r'Please provide values for N, L, '+u'\u03B2\u2080,'+u' \u03B2\u2081')
    quit()
print(sys.argv)

# Set parameter values
N = int(sys.argv[1])
L = int(sys.argv[2])
beta_0 = int(sys.argv[3])
beta_1 = int(sys.argv[4])
#grid

# Initialize beta grid
beta_0_grid = np.linspace(-10,10,100)
beta_1_grid = np.linspace(-10,10,100)

# Run functions to create x & y and plot
x,y            = md.makexy(N,L,beta_0,beta_1)
x_0,beta_1_new = md.getxandbeta1(x,y)
beta_0_new     = md.getbeta0(x_0,beta_1)
likely_start   = md.likeli(beta_0_new,beta_1_new)

md.makexyplot(x,y,x_0,beta_1_new)
plt.show()

# Optimize beta parameters
print('Initialized '+u'\u03B2\u2080 = ',beta_0_new,'and '+u'\u03B2\u2081 = ',beta_1_new)
print('Before approximation, L('+u'\u03B2\u2080,'+u'\u03B2\u2081) = ',likely_start)

# Maximize the likelihood by looping through grid
likely_best = 0.001
for i in range(0,len(beta_0_grid)):
    for j in range(0,len(beta_1_grid)):
        likely_new = md.likeli(beta_0_grid[i],beta_1_grid[j])
#        print(beta_0_grid[i],beta_1_grid[j],likely_new)
        if (likely_new > likely_best):
#            print(likely_start)
#            print(beta_0_grid[i],beta_1_grid[j],likely_new)
            beta_0_best = beta_0_grid[i]
            beta_1_best = beta_1_grid[j]
            likely_best = likely_new

print('Best values for '+u'\u03B2\u2080 = ',beta_0_best,' and '+u'\u03B2\u2081 =',beta_1_best)
print('With L('+u'\u03B2\u2080,'+u'\u03B2\u2081) = ',likely_best)
