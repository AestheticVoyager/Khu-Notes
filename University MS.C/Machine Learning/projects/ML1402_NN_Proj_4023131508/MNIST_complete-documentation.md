# MNIST from scratch
MNIST is a well-known dataset consisting of 28x28 pixel grayscale images of handwritten digits (0 through 9).
The goal of the neural network is to learn and predict the digit represented in each image.
The code uses a basic architecture with one hidden layer, ReLU activation for the hidden layer, and softmax activation for the output layer, adhering to standard practices for image classification problems.

## Using numpy
The code also uses standard functions like one-hot encoding, softmax activation, and ReLU activation, which are defined within the script.
While TensorFlow and scikit-learn are commonly used for such tasks, the code deliberately avoids using them to provide an example of implementing a neural network from scratch using basic numerical computation with NumPy.
The script trains the neural network using gradient descent and prints the loss for each epoch during training, followed by evaluating the accuracy on the test set.

## Recording Link
[link](https://drive.google.com/drive/folders/1j8dxdIk-yS2lx3HewK9ifiThJKBI-gxM?usp=sharing)

# Requirements
The requirements for running this code include having Python 3.12 installed on your system, along with the NumPy library for numerical operations.
Additionally, scikit-learn is used for fetching the MNIST dataset, splitting it into training and testing sets, and evaluating the model's accuracy.

```
pip install numpy,
pip install scikit-learn
```
