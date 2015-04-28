#Linear Least Squares Classifier

## Usage

`./LLS.py data_file [class_position]`

`data_file`
is a file containing data attributes and classes on each line,
 deliminated by a comma. Data must be formatted like those in the 
[UCI Repository](https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data).
Classes can be words or numbers.

`class_positon`
    Location in each line of the class label.
    Can be either head or tail. (Default: tail) 

# TODO
* Seperate classifier implementation from driver. Make it more of a "libary"
* Test on more datasets
* Add workaround if matrix inverse doesn't exit, flip coin if tie in class winner
* Improve docs

