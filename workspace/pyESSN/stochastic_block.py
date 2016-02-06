import numpy as np
import random

def stochastic_block(n, k=2, P, sizes, rca = True, v_out = False):
	#Input: 
	#   n = number of nodes
	#   k = number of blocks (default = 2)
	#   P = k x k matrix where the (i,j)th entry specifies the probability of connection between community i and j
	#   sizes = an array of length k where the ith entry specifies the size of the ith block. This must sum to n
	#   random.community.assignment = logical specifying whether or not the labels are assigned randomly. If FALSE, labels
	#                       are assigned in order starting with the upper left corner of the matrix.
	#   vector = logical specifying whether or not the returned adjacency matrix should be returned as a vector
	#            of edge variables. 
	#Output: 
	#   A list containing three components:
	#     Adjacency: the adjacency matrix of the generated network
	#     Membership: an n x 1 vector specifying community membership of each node

	if sum(sizes) != n:
		print "argument sizes must sum to n"

	if len(sizes) != k:
		print "argement sizes must be of length k"

	#generate membership
	labels = np.repeat(0,n)
	for i in range(1,n):
		z = np.cumsum(sizes)
		labels[z[i-1]:z[i]] = i

	Y = np.zeros([n,k])
	#@TODO allow edge list/adjacency matrix output
	#@TODO allow ability to toggle label assignment between random/ordered
	index = []
	possible = np.array(xrange(n))

	#assign labels randomly
	for i in xrange(k):
		index.append(random.sample(possible, sizes[i]))
		possible = np.setdiff1d(possible, update)
		labels[index[i]] = i

	for i in xrange(k):
		Y[index[i], i] = 1

	expected_A = np.matrix(Y) * np.matrix(P) * np.matrix(Y.T)
	expected_A[np.greater(expected_A,1)] = 1

	adj = np.random.binomial(1,expected_A.reshape([np.size(expected_A),1])).reshape(np.shape(expected_A))
	adj = adj * np.abs(np.eye(np.shape(expected_A)[0]) - 1)

	return [adj, labels]