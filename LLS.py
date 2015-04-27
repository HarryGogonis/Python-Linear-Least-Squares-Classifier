from numpy.linalg import inv, solve
import numpy as np
from milksets import wine

x,y = wine.load()

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

# fix data for homemade classifer
newY = []
for i in range(len(y)):
	size = max(y)
	temp = [0 for j in range(size + 1)]
	temp[y[i]] = 1
	newY.append(temp)
y = np.matrix(newY)


size = x.shape[0] - 1
# train with 50%
a = fit(x[size/2:],y[size/2:])

# test with 50%
i = size/2
misses = 0
hits = 0
for test_x in x[size/2:size] :
	prediction = predict(a,test_x)
	actual = list(y[i].A1)
	if prediction == actual:
		hits += 1
	else:
		misses += 1

total =  size/2 - 1
print hits, misses, total
accuracy = hits/float(hits+misses)*100
print accuracy, "%"
