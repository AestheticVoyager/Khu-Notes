from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

mnist = fetch_openml('mnist_784')
X, y = mnist.data / 255.0, mnist.target  # Normalize pixel values to be between 0 and 1

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=20, alpha=1e-4, solver='sgd', verbose=10, random_state=1, learning_rate_init=.1)

model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

