---
title: 'Linear Least Squares Classifier 1.0 documentation'
...

### Navigation

-   [Linear Least Squares Classifier 1.0
    documentation](index.html#document-index) »

Welcome to Linear Least Squares Classifier’s documentation![¶](#welcome-to-linear-least-squares-classifier-s-documentation "Permalink to this headline")
========================================================================================================================================================

Contents:

 `LLS.`{.descclassname}`fixLabels`{.descname}(*y*)[[source]](_modules/LLS.html#fixLabels)[¶](#LLS.fixLabels "Permalink to this definition")
:   Fixes labels so they fit our methods :param y: List of numbers
    cooresponding to class of each :return: Matrix of 0/1 lists.

    > Index in list with 1 is class of the cooresponding data Example:
    > [0 1 2] =\> [[1 0 0], [0 1 0], [0 0 1]]

 `LLS.`{.descclassname}`main`{.descname}()[[source]](_modules/LLS.html#main)[¶](#LLS.main "Permalink to this definition")
:   

 `LLS.`{.descclassname}`predict`{.descname}(*W*, *x*)[[source]](_modules/LLS.html#predict)[¶](#LLS.predict "Permalink to this definition")
:   Predict the class y of a single set of attributes :param W: DxK
    Least squares weight matrix :param x: 1xD matrix of attributes for
    testing :return: List of 0’s and 1’s. Index with 1 is the class of x

 `LLS.`{.descclassname}`test`{.descname}(*a*, *b*, *split*)[[source]](_modules/LLS.html#test)[¶](#LLS.test "Permalink to this definition")
:   Runs the linear least squares classifier :param a: All the data
    :param b: All the classes corresponding to data :param split: Where
    to split data for training

    > Ex: 40 trains with 40% and tests with 60%

 `LLS.`{.descclassname}`train`{.descname}(*x*, *y*)[[source]](_modules/LLS.html#train)[¶](#LLS.train "Permalink to this definition")
:   Build the linear least weight vector W :param x: NxD matrix
    containing N attributes vectors for training :param y: NxK matrix
    containing N class vectors for training

 `LLS.`{.descclassname}`usage`{.descname}()[[source]](_modules/LLS.html#usage)[¶](#LLS.usage "Permalink to this definition")
:   

Indices and tables[¶](#indices-and-tables "Permalink to this headline")
=======================================================================

-   [Index](genindex.html)
-   [Module Index](py-modindex.html)
-   [Search Page](search.html)

### [Table Of Contents](index.html#document-index)

©2015, Haralambos Gogonis. | Powered by [Sphinx
1.3.1](http://sphinx-doc.org/) & [Alabaster
0.7.3](https://github.com/bitprophet/alabaster)
