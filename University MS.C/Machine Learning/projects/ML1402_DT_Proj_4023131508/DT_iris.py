# Mahan Fallah - 4023131508
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth

    def fit(self, X, y, depth=0):
        if len(set(y)) == 1:
            # If all labels are the same, create a leaf node
            return {'class': y[0]}

        if self.max_depth is not None and depth == self.max_depth:
            # If maximum depth is reached, create a leaf node with the majority class
            return {'class': np.argmax(np.bincount(y))}

        # Find the best split
        best_split = self.find_best_split(X, y)

        if best_split is None:
            # If no split is found, create a leaf node with the majority class
            return {'class': np.argmax(np.bincount(y))}

        feature_index, threshold = best_split

        # Recursively build subtrees
        left_subset = X[:, feature_index] <= threshold
        right_subset = ~left_subset

        left_tree = self.fit(X[left_subset], y[left_subset], depth + 1)
        right_tree = self.fit(X[right_subset], y[right_subset], depth + 1)

        return {'feature_index': feature_index, 'threshold': threshold,
                'left': left_tree, 'right': right_tree}

    def find_best_split(self, X, y):
        m, n = X.shape
        if m <= 1:
            return None

        num_classes = len(set(y))
        if num_classes == 1:
            return None

        best_gini = float('inf')
        best_split = None

        for feature_index in range(n):
            thresholds = sorted(set(X[:, feature_index]))

            for threshold in thresholds:
                left_subset = X[:, feature_index] <= threshold
                right_subset = ~left_subset

                if sum(left_subset) > 0 and sum(right_subset) > 0:
                    gini = self.calculate_gini(y[left_subset], y[right_subset])
                    if gini < best_gini:
                        best_gini = gini
                        best_split = (feature_index, threshold)

        return best_split

    def calculate_gini(self, left_labels, right_labels):
        m = len(left_labels) + len(right_labels)
        gini_left = 1.0 - sum([(np.sum(left_labels == c) / len(left_labels))**2 for c in set(left_labels)])
        gini_right = 1.0 - sum([(np.sum(right_labels == c) / len(right_labels))**2 for c in set(right_labels)])
        gini = (len(left_labels) / m) * gini_left + (len(right_labels) / m) * gini_right
        return gini

    def predict_instance(self, tree, instance):
        if 'class' in tree:
            return tree['class']

        feature_index, threshold = tree['feature_index'], tree['threshold']

        if instance[feature_index] <= threshold:
            return self.predict_instance(tree['left'], instance)
        else:
            return self.predict_instance(tree['right'], instance)

    def predict(self, X):
        return [self.predict_instance(self.tree, instance) for instance in X]


# Example usage with Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the decision tree model
dt_model = DecisionTree(max_depth=3)
dt_model.tree = dt_model.fit(X_train, y_train)

# Make predictions on the test set
predictions = dt_model.predict(X_test)

# Evaluate accuracy
accuracy = np.mean(predictions == y_test)
print(f"Accuracy: {accuracy}")

