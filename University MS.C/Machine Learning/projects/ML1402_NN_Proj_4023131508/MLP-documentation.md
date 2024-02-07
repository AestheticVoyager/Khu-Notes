# Customizable Multi-Layer Perceptron NN from scratch
This is a simple implementation of a multi-layer perceptron (MLP) neural network in Python using NumPy. The neural network supports customizable parameters such as the number of layers, nodes in each layer, activation function, and learning rate.

The provided example demonstrates training a neural network on a simple dataset, showcasing how to create, train, and utilize the implemented MLP. Users can experiment with different architectures, activation functions, and learning rates to adapt the neural network for various tasks.

## Implementation Overview
The neural network is designed to be customizable, allowing users to specify the number of layers, nodes in each layer, activation function, and learning rate. 
It includes forward and backward propagation methods for training on a given dataset, and a prediction method for making predictions on new data after training.

To use the code, users can instantiate the `NeuralNetwork` class with their desired network architecture and hyperparameters. 
The neural network is then trained on a dataset using the `train` method, where both the input data (`X`) and target output (`Y`) matrices need to be provided. 
The number of training epochs is customizable, allowing users to control the training iterations. After training, the neural network can make predictions on new data using the `predict` method.

## Recording Link
[link](https://drive.google.com/drive/folders/1j8dxdIk-yS2lx3HewK9ifiThJKBI-gxM?usp=sharing)

## NeuralNetwork Class

## `__init__(self, layers, activation='sigmoid', learning_rate=0.01)`
```
- Initializes the neural network.
- Parameters:
  - layers: List of integers specifying the number of nodes in each layer.
    - activation: String, activation function type ('sigmoid', 'relu', 'tanh').
      - learning_rate: Float, learning rate for gradient descent.
```
## `forward_propagation(self, x) -> np.ndarray`
      - Performs forward propagation through the neural network.
      - Parameters:
        - x: Input data for a single training example.
        - Returns:
          - np.ndarray: Output of the neural network.

## `backward_propagation(self, x, y) -> None`
          - Performs backward propagation to update weights and biases.
          - Parameters:
            - x: Input data for a single training example.
              - y: Target output for the corresponding training example.

## `train(self, X, Y, epochs=1000) -> None`
              - Trains the neural network on the provided dataset.
              - Parameters:
                - X: Input data matrix (features as columns).
                  - Y: Target output matrix (corresponding to each input).
                    - epochs: Number of training iterations.

## `predict(self, x) -> np.ndarray`
                    - Makes predictions using the trained neural network.
                    - Parameters:
                      - x: Input data for prediction.
                      - Returns:
                        - np.ndarray: Predicted output.