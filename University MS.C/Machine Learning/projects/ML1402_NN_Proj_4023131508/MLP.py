# 4023131508 Mahan Fallah
import numpy as np

class NeuralNetwork:
    def __init__(self, layers, activation='sigmoid', learning_rate=0.01):
        self.layers = layers
        self.num_layers = len(layers)
        self.weights = [np.random.randn(layers[i], layers[i-1]) for i in range(1, self.num_layers)]
        self.biases = [np.zeros((layers[i], 1)) for i in range(1, self.num_layers)]
        self.activation_function = self._get_activation_function(activation)
        self.learning_rate = learning_rate

    # Returns the specified activation function as a lambda function
    def _get_activation_function(self, activation):
        if activation == 'sigmoid':
            return lambda x: 1 / (1 + np.exp(-x))
        elif activation == 'relu':
            return lambda x: np.maximum(0, x)
        elif activation == 'tanh':
            return lambda x: np.tanh(x)
        else:
            raise ValueError(f"Activation function '{activation}' not supported.")

    # Performs forward propagation through the network
    # Iterates through layers, calculates weighted sum, applies activation function, and updates input and output lists.
    # Returns the final output of the network.
    def forward_propagation(self, x):
        self.inputs = [x]
        self.outputs = []

        for i in range(self.num_layers-1):
            z = np.dot(self.weights[i], self.inputs[-1]) + self.biases[i]
            a = self.activation_function(z)
            self.outputs.append(z)
            self.inputs.append(a)

        return self.inputs[-1] 

    # Performs backwrd propagation through the network
    # Calculates gradients for weights and biases using the mean squared error loss.
    # Updates weights and biases using gradient descent.
    # Iterates backward through layers, computing gradients, and updating parameters.
    def backward_propagation(self, x, y):
        m = x.shape[1] # Number of training examples
        dz = self.inputs[-1]-y
        dw = np.dot(dz, self.inputs[-2].T)/m
        db = np.sum(dz, axis=1, keepdims=True)/m

        self.weights[-1] -= self.learning_rate * dw
        self.biases[-1] -= self.learning_rate * db

        for i in range(self.num_layers-2, 0, -1):
            dz = np.dot(self.weights[i].T, dz) * (1-self.activation_function(self.outputs[i-1])**2)
            dw = np.dot(dz, self.inputs[i-1].T)/m
            db = np.sum(dz, axis=1, keepdims=True)/m

            self.weights[i-1] -= self.learning_rate * dw
            self.biases[i-1] -= self.learning_rate * db
            
    # Trains the neural network using provided input(X) and target(Y) data.
    # Epochs: Number of training iterations.
    # Nested loop for iterating through epochs and tarining example.
    def train(self, X, Y, epochs=1000):
        for epoch in range(epochs):
            for i in range(X.shape[1]):
                x = X[:, i].reshape(-1, 1)
                y = Y[:, i].reshape(-1, 1)
                '''
                This line is extracting the i-th training example from the input data Y and reshaping it into a colum vector y, which is then used as input for the neural network during training.
                '''

                # Calls Forward Propagation and Backward Propagation for each training example.
                self.forward_propagation(x)
                self.backward_propagation(x, y)
                
    # Makes Predictions using the trained network
    # Calls Forward_propagation with input X
    def predict(self, x):
        return self.forward_propagation(x)

# Example Code
input_size = 2
hidden_size = 3
output_size = 1

nn = NeuralNetwork(layers=[input_size, hidden_size, output_size], activation='sigmoid', learning_rate=0.01)

X_train = np.array([[0,0], [0,1], [1,0], [1,1]]).T
Y_train = np.array([[0, 1, 1, 0]])

nn.train(X_train, Y_train, epochs=10000)

for i in range(X_train.shape[1]):
    prediction = nn.predict(X_train[:, i].reshape(-1, 1))
    print(f"Input: {X_train[:, i]}, Prediction: {prediction}")
