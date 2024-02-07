# K-Nearest Neighbors for Iris 

Implementation of K-Nearest Neighbors (KNN) classifier for the Iris dataset using the scikit-learn library.
The Iris dataset comprises measurements of sepal and petal dimensions for three species of iris flowers.
The primary goal of the script is to predict the species based on these features.
The code loads the dataset, splits it into training and testing sets, creates a KNN classifier with a k-value of 3, trains the classifier on the training set, and evaluates its performance on the test set, providing accuracy metrics and a detailed classification report.

```python
# 4023131508 Mahan Fallah
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

iris = datasets.load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

knn_classifier = KNeighborsClassifier(n_neighbors=3)

knn_classifier.fit(X_train, y_train)

y_pred = knn_classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n", classification_rep)
```