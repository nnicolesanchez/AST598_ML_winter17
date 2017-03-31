Astronomy 598: Machine Learning (Winter 2017)
Student: Natalie Nicole Sanchez
Using Python 3.5.2
___________________________

Problem Set #6
___________________________

Part a:
Run program crossvalidate5.py
$ python crossvalidate5.py

*Limitations: Only viable for k=5 fold

The average MSE for a 5 k-fold cross-val:
0.479

Part b:
To determine a model for a generated data set, we could attempt
to examine the average MSE values for different model types. For 
example, applying a quadratic model or a sinusoidal model results 
in average MSE values of ~39 and ~6, respetively, indicating that
neither of these models is as valid as the linear (y=ax+b) model.
However, testing arbitrary models for a data set and minimizing 
the MSE might prove too time intensive. A better method would 
include plotting the data and attempting to fit a function.

#### EDITED 02.27.17 ####
$ python crossvalidate5.py 

Now it calculates a & b within the script rather than using the
a & b values directly from HW#1.
