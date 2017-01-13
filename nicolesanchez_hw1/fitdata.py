# This script reads in the output of makedata.py
#      N = [x_i,y_i]
# Uses the least squares method to fit the data

# Writes out the values for a and b
import matplotlib.pyplot as plt
import numpy as np
import sys

if len(sys.argv) < 2:
    print(r'Please provide a data.out file')
    quit()
print(sys.argv)

pairs = np.loadtxt(sys.argv[1])
pairs = np.transpose(pairs)

x = pairs[0]
y = pairs[1]

x_mean = np.mean(x)
y_mean = np.mean(y)

def a(y,x):
    b_1 = (np.average(x*y) - (x_mean*y_mean))/(np.average(x**2.) - (x_mean**2.))
    return b_1

def b(y,x,b_1):
    b_0 = y_mean - (b_1*x_mean)
    return b_0

a = a(y,x)
b = b(y,x,a)

print('Estimated value of a: ',a)
print('Estimated value of b: ',b)

y_new = b + (x*a) 

plt.plot(x,y,'.',markersize=8,color='SteelBlue',label='Test Data Points')
plt.plot(x,y_new,linewidth=1,color='Salmon',label='Least Squares Linear Regression')
plt.legend(loc=4)
plt.title('N = 1000')
plt.ylabel('y')
plt.xlabel('x')
plt.ylim(1,13)
plt.savefig('plot_datafits_'+str(sys.argv[1])+'.ps')
plt.show()


# Residuals
res = y - (a*x) - b 

plt.plot(x,res,'.',color='SteelBlue')
plt.title('N = 1000, residuals')
plt.ylabel('residuals')
plt.xlabel('x')
plt.savefig('plot_residuals_'+str(sys.argv[1])+'.ps')
plt.show()
