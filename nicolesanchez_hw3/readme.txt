Astronomy 598: Machine Learning (Winter 2017)
Student: Natalie Nicole Sanchez
Using Python 3.5.2
___________________________

Problem Set #3
___________________________

To run program: makedata.py
You will run "python makedata.py" and supply "N mu sigma"

For Part c:
$ python makedata.py 1000 0 1

This script creates the data.out file which we will later 
call for our bootstrapping algorithm.
* Limitations: Requires input parameters.

For Part d:
$ python findmean.py

Computes and prints the mean for data.out file (x array).
* Limitations: must have a data.out file in directory to run.

############################
To run program: bootstrap.py
You will run "python bootstrap.py" and supply "M"

For Part e:
$ python bootstrap.py 10

This script creates the boot10.out files.
* New output files are produced if M is varied (e.g. boot100.out)
* Limitations: Requires input M value.

############################
To run program: bootstrap.py
You will run "python bootstrap.py" and supply "M"

For Part f:
$ python bootplot.py 10

This script creates the	bootplot10.ps plot file.	
* New plots are produced if M is varied (e.g. bootplot100.ps)
* Limitations: Requires input M value.

For Part g:
A sufficiently large value for M is M = 100. The distribution is smooth at this point,
unlike the way it is for M = 10. Increasing M makes only makes the distribution smoother,
as noted in the homework instructions. 
