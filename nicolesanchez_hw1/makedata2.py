# This script makes the data for problem set 1
#      N, number of pairs of points
#      e, noise/error term, random variable from Gaussian dist.
#      mu,  mean of e
#      sigma, standard deviation, *assuming standard deviation is ind of x

# Writes out data.out
import numpy as np
import sys
#print(sys.argv)

if len(sys.argv) < 5:
    print(r'Please provide values for N, a, b, '+u'\u03BC, c')
    quit()
print(sys.argv)

N     = int(sys.argv[1])
a     = float(sys.argv[2])
b     = float(sys.argv[3])
mu    = float(sys.argv[4])
c     = float(sys.argv[5])

x = np.random.uniform(0.0,10.0,N)
sigma = c*x
e = np.random.normal(mu, sigma)

def y_i(x,e):
    y = (a*x) + b + e
    return y

y = y_i(x,e)

pairs = [x,y]
pairs = np.transpose(pairs)
print(pairs)

np.savetxt('data2.out',pairs)


