Astronomy 598: Machine Learning (Winter 2017)
Student: Natalie Nicole Sanchez
Using Python 3.5.2
___________________________

To run program: makedata.py
You will run "python makedata.py" and supply "N a b mu sigma"

For Part c:
$ python makedata.py 1000 1 2 0 0.1

This script creates data.out.
*Limitations: Requires N, a, b, mu, and sigma to be supplied.
	      No variation for x range.

For Part D:
$ python fitdata.py data.out

This script creates the plots for Part e and f.
*Limitations: Requires a data file input.

For Part F:
    The range of the residuals are small (between -2.e-15 and 2e-15). The plot is stratified at intervals around 5e-14. 

____________________________

To run program: makedata2.py
You will run "python makedata2.py" and supply "N a b mu sigma"

For Part H:
$ python makedata2.py 1000 1 2 0 0.1

This script creates data.out.
*Limitations: Requires N, a, b, mu, and c to be supplied.
              No variation for x range.

For Part I:
$ python fitdata.py data2.out

This script creates the plots for Part j and k.
*Limitations: Requires a data file input.

For Part f:
    The range of the residuals are larger in this case (-3 to 3). The plot has a much wider spread, smaller at low values of x and increasing as x increases (similar to the preceding x vs y plot).
