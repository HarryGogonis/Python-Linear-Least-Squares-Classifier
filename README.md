#Linear Least Squares Classifier

## Usage

`./LLS.py data_file [--head]`

`data_file`
is a file containing data attributes and classes on each line,
 deliminated by a comma. Data must be formatted like those in the 
[UCI Repository](https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data).
Classes can be words or numbers.

`--head`
    (optional) Explicitly state the location of the class label is 
	at the head of each line. Without this option,
	default to the tail of the line.
	If you are getting terrible accuracy, you may have forgot to enable this flag.

# TODO
* Seperate classifier implementation from driver. Make it more of a "libary"
* Test on more datasets
* Add workaround if matrix inverse doesn't exit, flip coin if tie in class winner
* Improve docs

