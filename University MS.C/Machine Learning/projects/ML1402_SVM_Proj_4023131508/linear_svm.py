import numpy as np
from cvxopt import matrix, solvers

class LinearSVM:
    def __init__(self):
        self.alpha = None  # Lagrange multipliers
        self.support_vectors = None
        self.support_labels = None
        self.w = None
        self.b = 0

    def fit(self, X, y):
        n_samples, n_features = X.shape

        # Calculate the kernel (here it's linear, so it's just the dot product)
        K = np.dot(X, X.T)

        # Set up the parameters for the convex optimization problem
        P = matrix(np.outer(y, y) * K)
        q = matrix(-np.ones(n_samples))
        G = matrix(-np.eye(n_samples))  # This enforces the constraint 0 <= alpha
        h = matrix(np.zeros(n_samples))  # No upper bound for hard margin
        A = matrix(y, (1, n_samples), 'd')
        b = matrix(0.0)

        # Solve the QP problem using CVXOPT
        solvers.options['show_progress'] = False
        solution = solvers.qp(P, q, G, h, A, b)

        # Extract the Lagrange multipliers
        alphas = np.ravel(solution['x'])

        # Support vectors have non zero lagrange multipliers
        sv = alphas > 1e-5
        ind = np.arange(len(alphas))[sv]
        self.alpha = alphas[sv]
        self.support_vectors = X[sv]
        self.support_labels = y[sv]

        # Calculate the weights w
        self.w = np.dot(self.support_vectors.T, self.alpha * self.support_labels)

        # Calculate the intercept b
        self.b = np.mean(self.support_labels - np.dot(self.support_vectors, self.w))

