"""
Find the stationary distribution of Markov Chain Process
"""

import numpy as np

#note: the matrix is row stochastic.
#A markov chain transition will correspond to left multiplying by a row vector.
n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    row_sum = sum(row)
    for i in range(n):
        row[i] = row[i]/row_sum
    matrix.append(row)

matrix = np.array(matrix)


#We have to transpose so that Markov transitions correspond to right multiplying by a column vector.  np.linalg.eig finds right eigenvectors.
evals, evecs = np.linalg.eig(matrix.T)
evec1 = evecs[:,np.isclose(evals, 1)]  # choose one with 1 eigenvalue

#Since np.isclose will return an array, we've indexed with an array
#so we still have our 2nd axis.  Get rid of it, since it's only size 1.
evec1 = evec1[:,0]

stationary = evec1 / evec1.sum()

#eigs finds complex eigenvalues and eigenvectors, so you'll want the real part.
stationary = stationary.real
stationary = list(map(round, stationary, [2 for _ in range(len(stationary))]))

print(*stationary)