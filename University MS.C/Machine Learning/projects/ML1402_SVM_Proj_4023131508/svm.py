# Mahan Fallah - 4023131508
import numpy as np
from cvxopt import matrix, solvers
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

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

    def predict(self, X):
        return np.sign(np.dot(X, self.w) + self.b)

# Example usage:
# Assuming you have your data X and labels y
svm_model = LinearSVM()
svm_model.fit(X, y)

# Now you can access the trained model parameters
print("Optimal Weights (w):", svm_model.w)
print("Optimal Bias (b):", svm_model.b)

# Split the data into training (60%) and test (40%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Make predictions on training data
train_predictions = svm_model.predict(X_train)

# Make predictions on test data
test_predictions = svm_model.predict(X_test)

# Calculate confusion matrix and accuracy for training data
conf_matrix_train = confusion_matrix(y_train, train_predictions)
accuracy_train = accuracy_score(y_train, train_predictions)

# Calculate confusion matrix and accuracy for test data
conf_matrix_test = confusion_matrix(y_test, test_predictions)
accuracy_test = accuracy_score(y_test, test_predictions)

# Print the results
print("\nConfusion Matrix (Training Data):")
print(conf_matrix_train)
print("Accuracy (Training Data):", accuracy_train)

print("\nConfusion Matrix (Test Data):")
print(conf_matrix_test)
print("Accuracy (Test Data):", accuracy_test)

