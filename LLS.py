#!/usr/bin/env python
from numpy.linalg import inv, solve
import numpy as np
import sys, os
from random import shuffle


# Build weight vector w
def fit(x,y):
	D = x.shape[1] + 1
	K = y.shape[1]
	sum1 = np.zeros((D,D))
	sum2 = np.zeros((D,K))
	i = 0
	# build weight vector
	for x_i in x:
		x_i = np.append(1, x_i) # augment vector with a 1 
		y_i = y[i]
		sum1 += np.outer(x_i, x_i)		# find xi*xi_T
		sum2 += np.outer(x_i, y_i)
		i += 1
	return np.dot(inv(sum1),sum2)	# return weight vector


def predict(W, x):
	x = np.append(1, x)
	values = np.dot(W.T,x)
	# winner take all
	values = list(values)
	winner = max(values)
	#TODO if tie, toss a coin
	y = [0 for x in values]
	y[values.index(winner)] = 1
	return y

# fix labels so it fits homemade classifer
# Ex: 3 becomes [0 0 1]
def fixLabels(y):
	newY = []
	for i in range(len(y)):
		size = max(y)
		temp = [0 for j in range(size + 1)]
		temp[y[i]] = 1
		newY.append(temp)
	return np.matrix(newY)

def test(a,b, split):
	W = fit(a[:split],b[:split])
	x = a[split:]
	y = b[split:]
	total = y.shape[0]
	i = 0
	hits = 0
	for i in range(total):
		prediction = predict(W,x[i])
		actual = list(y[i].A1)
		if prediction == actual:
			hits += 1
	accuracy = hits/float(total)*100
	print "Accuracy = " + str(accuracy) + "%", "(" + str(hits) + "/" + str(total) + ")"

def usage():
	return 'usage: %s <data file> [head/tail]\n' % os.path.basename( sys.argv[ 0 ] )

def main():
	# Load Data
	#x,y = wine.load()
	#y = fixLabels(y)
	
	if len(sys.argv) < 2:
		print usage()
		sys.exit(1)
	
	head = False
	if "--head" in sys.argv:
		head = True
	
	data = []
	classes = []
	f = open(sys.argv[1]) # open file
	try:
		for line in f:
			if line == "\n" or line == "": continue # skip empty lines
			line = line.strip("\n").split(",")		# split line
			if head:
				# Convert raw data to float and add to data list
				data.append(map(lambda x: float(x), line[0:]))
				# Add class to list
				classes.append(line[0])
			else:
				# Convert raw data to float and add to data list
				data.append(map(lambda x: float(x), line[:-1]))
				# Add class to list
				classes.append(line[-1])
	finally:
		f.close()
	
	classTypes = list(set(classes)) # list of distinct class types
	# Convert class names to number
	classes = map(lambda x: classTypes.index(x), classes)
	
	x = np.matrix(data)
	y = fixLabels(classes)

	size = x.shape[0] - 1

	# shuffle data
	z = []
	for i in range(size):
		z.append((x[i],y[i]))
	shuffle(z)
	for i in range(size):
		x[i] = z[i][0]
		y[i] = z[i][1]
		
	# scale data
	for i in range(size):
		x[i] = x[i] / x.max()
	
	# train/test data
	#90/10 
	print "90% Train/10% Test"
	split = int(size * 0.9)
	test(x,y,split)
	print "------------------\n"
	#60/30
	print "60% Train/30% Test"
	split = int(size * 0.6)
	test(x,y,split)
	print "------------------\n"
	# 50/50	
	print "50% Train/50% Test"
	split = int(size * 0.5)
	test(x,y,split)
	print "------------------\n"
	# 30/60
	print "30% Train/60% Test"
	split = int(size * 0.3)
	test(x,y,split)
	print "------------------\n"
	# 10/90
	print "10% Train/90% Test"
	split = int(size * 0.1)
	test(x,y,split)
	print "------------------\n"
if __name__ == "__main__":
	main()
