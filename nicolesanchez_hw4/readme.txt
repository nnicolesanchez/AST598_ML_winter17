Astronomy 598: Machine Learning (Winter 2017)
Student: Natalie Nicole Sanchez
Using Python 3.5.2
___________________________

Problem Set #4
___________________________

To run programs:

$ python maketrain.py

This script creates the iris.train and 
iris.test outputs.

$ python splittrain.py

This script creates the iris.setosa, 
iris.versicolor, and iris.virginica outputs.

$ python trykde.py 0.1

This script creates the kde.out output. 
* Limitations: Requires bandwidth input.
  	       'python trykde.py h_value'

For Part h:
For all except two values in the iris.test case (index 2 & 6)
the Iris Type for the highest KDE value is the same as the 
real classification. In these two cases (n=2,6), the KDE-setosa
value is 0.0000 possibly indicating some other error in the
KDE calculation and resulting in the misclassification.
