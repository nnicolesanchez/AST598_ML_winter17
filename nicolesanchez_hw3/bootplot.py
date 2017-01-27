# This script uses the boot.out mean values to create a distribution

# N. Nicole Sanchez      -- AST 598: Machine Learning
# Univ. of Wash, Seattle -- Problem Set 3
import matplotlib.pyplot as plt
import scipy.signal as sci
import numpy as np
import sys

if len(sys.argv) != 2:
    print(r'Please provide M, resampling size.')
    print('(For which bootstrap.py has been run)')
    quit()
M = sys.argv[1]
means = np.loadtxt('boot'+str(M)+'.out')

plt.hist(means)#,bins=100)
plt.ylabel('dN/dmeans')
plt.xlabel('Means')
plt.savefig('bootplot'+M+'.ps')
plt.show()
