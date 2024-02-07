# Mahan Fallah - 4023131508
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler, LabelBinarizer

def one_hot_encode(y, num_classes):
    label_binarizer = LabelBinarizer()
    label_binarizer.fit(range(num_classes))
    encoded = label_binarizer.transform(y)
    return encoded

def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=1, keepdims=True)

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)

# Load the MNIST dataset
mnist = fetch_openml('mnist_784')
X, y = mnist.data / 255.0, mnist.target  # Normalize pixel values to be between 0 and 1

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data (optional but can be beneficial)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# One-hot encode the labels
num_classes = 10  # Assuming 10 classes (digits 0 through 9)
y_train_encoded = one_hot_encode(y_train.astype(int), num_classes)
y_test_encoded = one_hot_encode(y_test.astype(int), num_classes)

# Define neural network architecture
input_size = X_train.shape[1]
hidden_size = 128
output_size = num_classes

# Initialize weights and biases with Xavier/Glorot initialization
np.random.seed(42)
weights_input_hidden = np.random.randn(input_size, hidden_size) / np.sqrt(input_size)
biases_input_hidden = np.zeros((1, hidden_size))
weights_hidden_output = np.random.randn(hidden_size, output_size) / np.sqrt(hidden_size)
biases_hidden_output = np.zeros((1, output_size))

# Hyperparameters
learning_rate = 0.001  # Adjust the learning rate
epochs = 20  # Increase the number of epochs

# Training the neural network
for epoch in range(epochs):
    # Forward pass
    hidden_layer_input = np.dot(X_train, weights_input_hidden) + biases_input_hidden
    hidden_layer_output = relu(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + biases_hidden_output
    predicted_probabilities = softmax(output_layer_input)

    # Compute loss (cross-entropy loss)
    loss = -np.sum(y_train_encoded * np.log(np.clip(predicted_probabilities, 1e-10, 1.0))) / len(X_train)

    # Backward pass
    output_error = predicted_probabilities - y_train_encoded
    hidden_layer_error = np.dot(output_error, weights_hidden_output.T) * relu_derivative(hidden_layer_input)

    # Update weights and biases using gradient descent with L2 regularization
    weights_hidden_output -= learning_rate * (np.dot(hidden_layer_output.T, output_error) / len(X_train) + 0.001 * weights_hidden_output)
    biases_hidden_output -= learning_rate * np.sum(output_error, axis=0, keepdims=True) / len(X_train)
    weights_input_hidden -= learning_rate * (np.dot(X_train.T, hidden_layer_error) / len(X_train) + 0.001 * weights_input_hidden)
    biases_input_hidden -= learning_rate * np.sum(hidden_layer_error, axis=0, keepdims=True) / len(X_train)

    # Print loss for every epoch
    print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss}")

# Make predictions on the test set
hidden_layer_input_test = np.dot(X_test, weights_input_hidden) + biases_input_hidden
hidden_layer_output_test = relu(hidden_layer_input_test)
output_layer_input_test = np.dot(hidden_layer_output_test, weights_hidden_output) + biases_hidden_output
predicted_probabilities_test = softmax(output_layer_input_test)
y_pred = np.argmax(predicted_probabilities_test, axis=1)

# Calculate accuracy
accuracy = accuracy_score(y_test.astype(int), y_pred)
print(f"Accuracy: {accuracy}")

