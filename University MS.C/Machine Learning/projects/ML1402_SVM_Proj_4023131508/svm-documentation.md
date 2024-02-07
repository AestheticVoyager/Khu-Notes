# SVM Classifier with Quadratic Programming Solver

This code provides a simple implementation of a linear Support Vector Machine (SVM) classifier using a quadratic programming solver. 
The SVM is trained to classify data into two classes.
`svm.py` file contains the answer to both problems.

## Overview

The code consists of a Python class `LinearSVM`, which is responsible for training the SVM using a quadratic programming solver. The solver is based on the CVXOPT library.
This code now includes the predict method in the LinearSVM class, and it demonstrates how to use the classifier to make predictions on both training and test data, followed by the calculation of the confusion matrix and accuracy for each set.

## Recording Link
[link](https://drive.google.com/drive/folders/1j8dxdIk-yS2lx3HewK9ifiThJKBI-gxM?usp=sharing)

## Requirements

To run this code, you need the following dependencies:

- Python 3.x
- NumPy
- CVXOPT

You can install the required packages using the following command:

```bash
pip install numpy cvxopt
```

## How to Use

1. Import the `LinearSVM` class in your Python script or Jupyter Notebook.
2. Create an instance of the `LinearSVM` class.
3. Call the `fit` method on the instance, passing your data matrix `X` and corresponding labels `y`.
4. Access the trained SVM parameters using the instance attributes: `w` (weights), `b` (bias).

```python
from linear_svm import LinearSVM

# Assuming you have your data X and labels y
svm_model = LinearSVM()
svm_model.fit(X, y)

# Access the trained model parameters
print("Optimal Weights (w):", svm_model.w)
print("Optimal Bias (b):", svm_model.b)
```

## Notes
Make sure to create a `linear_svm.py` file containing your `LinearSVM` class and adjust the filenames and paths accordingly. 

- The SVM is trained using a linear kernel.
- The `fit` method uses a quadratic programming solver from the CVXOPT library to find Lagrange multipliers and calculate the SVM parameters.

