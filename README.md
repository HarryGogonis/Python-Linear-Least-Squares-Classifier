#Linear Least Squares Classifier

### Requirements
* Python - tested with version 2.7.6
* [Numpy](http://docs.scipy.org/doc/numpy/user/index.html) - tested with version 1.8.2

### Usage

`./LLS.py data_file [--head]`

`data_file`
is a file containing data attributes and classes on each line,
deliminated by a comma.

* Data must be formatted like those in the 
[UCI Repository](https://archive.ics.uci.edu/ml/datasets.html).
* Example data sets from UCI are included in the repo:
[iris.csv](https://bitbucket.org/cot4501group3/least-squares-classifier/src/c2922f380e70ae6b27532103fe8590a192c66a0d/iris.csv?at=master) and
[wine.csv](https://bitbucket.org/cot4501group3/least-squares-classifier/src/c2922f380e70ae6b27532103fe8590a192c66a0d/wine.csv?at=master)
* Classes can be words or numbers. **Attributes must be numbers at this time**

`--head`
    (optional) Explicitly state the location of the class label is 
	at the head of each line. Without this option,
	default to the tail of the line.
	If you are getting terrible accuracy, you may have forgot to enable this flag.

You can also run all the data sets in this repo by executing `run_data.sh`