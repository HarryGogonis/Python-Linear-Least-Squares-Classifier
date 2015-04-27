from numpy.linalg import inv, solve
import numpy as np
from milksets import wine


# Build weight vector w
def fit(x,y):
	D = x[0].size + 1
	K = y[0].size 
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

	return inv(sum1).dot(sum2)	# return weight vector


def predict(W, x):
	x = np.append([1], x)
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

def test(x,y, split):
	W = fit(x[:split],y[split:])
	x = x[split:]
	y = y[split:]
	
	i = 0
	misses = 0
	hits = 0
	for test_x in x :
		prediction = predict(W,test_x)
		actual = list(y[i].A1)
		if prediction == actual:
			hits += 1
		else:
			misses += 1

	accuracy = hits/float(hits+misses)*100
	print "Accuracy:", accuracy, "%"

def main():
	# Load Data
	x,y = wine.load()
	y = fixLabels(y)

	size = x.shape[0] - 1

	# 50/50	
	print "50% Train/50% Test"
	split = int(size * 0.5)
	test(x,y,split)
	# 30/60
	print "30% Train/60% Test"
	split = int(size * 0.3)
	test(x,y,split)
	# 10/90
	print "10% Train/90% Test"
	split = int(size * 0.1)
	test(x,y,split)

if __name__ == "__main__":
	main()
