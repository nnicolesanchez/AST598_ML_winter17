# This script contains the necessary functions for problem set 2
#      N, number of pairs of points
#      L, (-L,+L) values between which x is generated
#      beta_0, input parameter for likelihood
#      beta_1, input parameter for likelihood

# It also creates the x vs y plot as a .ps file

# N. Nicole Sanchez      -- AST 598: Machine Learning
# Univ. of Wash, Seattle -- Problem Set 2  
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import numpy as np
import sys

# Require input parameters 
if len(sys.argv) != 5:
    print(r'Please provide values for N, L, '+u'\u03B2\u2080,'+u' \u03B2\u2081')
    quit()
#print(sys.argv)

# Set input parameters
N = int(sys.argv[1])
L = int(sys.argv[2])
beta_0 = int(sys.argv[3])
beta_1 = int(sys.argv[4])

# Functions
def prob(x):
    p = 1/(1 + np.exp(-(beta_0 + beta_1*x)))
    return p

def makexy(N,L,beta_0,beta_1):
    x = np.random.uniform(-L,L,N)
    p = prob(x)
    y = np.random.binomial(1.0,p,size=len(x))
    return x,y 

def getxandbeta1(x,y):
    i  = np.where(y == 1)
    ip = np.where(y == 0)
    x_i_min  = np.min(x[i])
    x_ip_max = np.max(x[ip])
    beta_1_invnew = x_ip_max - x_i_min
    x_0  = x_i_min + (beta_1_invnew/2)

    beta_1_new = 1/beta_1_invnew
    return x_0,beta_1_new

def getbeta0(x_0,beta_1_new):
    beta_0_new = -(beta_1_new*x_0)
    return beta_0

def makeplotbox(x_0,beta_1_new):
    beta_1_invnew = 1/beta_1_new
    x_i_min = x_0 - (beta_1_invnew/2)
    box = pat.Rectangle((x_i_min,-1),np.abs(beta_1_invnew), 3, color='Salmon', alpha=0.5)    
    return box

def makexyplot(x,y,x_0,beta_1_new):
    box = makeplotbox(x_0,beta_1_new)
    
    x_0_line   = [x_0,x_0]
    y_x_0_line = [-2,2]
    
    fig = plt.figure()
    ax  = fig.add_subplot(111)#, aspect='equal')
    ax.plot(x,y,'.',color='SteelBlue')
    ax.plot(x_0_line,y_x_0_line,'--',color='Red')
    ax.add_patch(box)
    ax.set_ylim(-0.5,1.5)
    ax.set_xlim(-5,5)
    plt.savefig('xvsy_plot_N'+str(N)+'.ps')

def likeli(beta_0,beta_1):
    global N, L
    x,y = makexy(N,L,beta_0,beta_1)
    i  = np.where(y == 1)
    ip = np.where(y == 0)
    l = np.prod(prob(x[i]))*np.prod(1 - prob(x[ip]))
    return l

# Make x vs y plot
#x,y = makexy(N,L,beta_0,beta_1)
#x_0,beta_1_new = getxandbeta1(x,y)
#beta_0_new     = getbeta0(x_0,beta_1_new)

#makexyplot(x,y,x_0,beta_1_new)
#plt.show()
#plt.clf()

# Test likelihood function:
#print(u'\u03B2\u2080: ',1/beta_1_invnew)
#print('x'+u'\u2080: ',x_0)
#ell = likeli(beta_0,beta_1)
#print('Likelihood with '+u'\u03B2\u2080 = 2, '+u'\u03B2\u2081 = 3: ',ell)

