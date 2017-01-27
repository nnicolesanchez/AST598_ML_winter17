# This script uses the bootstrap method to get a distribution for
# estimated means. 
#      - Reads in N values of x from data.out
#      - Resamples x to get M new arrays
#          * may see some original points missing; some repeating
#      - Computes the mean of M resamples
#      - Save in file boot.out

# N. Nicole Sanchez      -- AST 598: Machine Learning
# Univ. of Wash, Seattle -- Problem Set 3
import matplotlib.pyplot as plt
import scipy.signal as sci
import numpy as np
import sys

if len(sys.argv) != 2:
    print(r'Please provide M, resampling size.')
    quit()
print(sys.argv)

M = int(sys.argv[1])

x = np.loadtxt('data.out')

means = []
for i in range(0,M):
    x_M    = np.random.choice(x,len(x),replace=True)
    mean_M = np.mean(x_M)
    means.append(mean_M)

print(means)
np.savetxt('boot'+str(M)+'.out',means)
