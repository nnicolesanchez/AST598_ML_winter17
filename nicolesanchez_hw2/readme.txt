Astronomy 598: Machine Learning (Winter 2017)
Student: Natalie Nicole Sanchez
Using Python 3.5.2
___________________________

Problem Set #2
___________________________

To run program: makedata.py
You will run "python makedata.py" and supply "N L beta0 beta1"

For Part c:
$ python makedata.py 1000 50 2 3

This script holds all the functions to create x & y and plot them.
* However, I instead use gridsearch.py to call and run the plotting
function to make sure my plot corresponds to each new randomly drawn 
distribution. The lines 84-90 can be un-commented out to plot using 
makedata.py specifically.

For Part d:
This script also holds the function to calculate likelihood given 
beta parameters. It can print out the likelihood for beta0 = 2 & beta1 = 3
Uncomment out lines 93-96 to see output similar to below.
Output: (Note: Likelihood changes with varying x)
   ['makedata.py', '1000', '50', '2', '3']
   β₀:  0.768559784262
   x₀:  -0.372566288371
   Likelihood with β₀ = 2, β₁ = 3:  5.02603947325e-06

* Also note: plot is limited to x-axis (-5,5) to better show the width
of the region where the function rises from 0 to 1 
___________________________

To run program: gridsearch
You will run "python gridsearch.py" and supply "N L beta0 beta1"

For Part e:
$ python gridsearch.py 1000 50 2 3

This script creates xvsy_plot_N1000.ps
* New plots are produced if N is varied (e.g. xvsy_plot_N500.ps)
* Limitations: Requires input parameters.
	       No variation for grid values.

For Part f: Maximum Likelihood Estimates
Output: (Note: These values change with every iteration because
               x is randomly selected each time)
   Initialized β₀ =  2 and β₁) = 1.01808710294
   Before approximation, L(β₀,β₁) =  0.00133417254106
   Best values for β₀ =  -5.35353535354  and β₁ = -8.78787878788
   With L(β₀,β₁) =  0.191781884405
