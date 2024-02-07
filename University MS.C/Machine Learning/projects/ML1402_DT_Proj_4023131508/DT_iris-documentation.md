# Decision Tree for IRIS classification
Implementation of a basic decision tree classifier for the Iris dataset. 

# Implementation Overview
The decision tree is a supervised machine learning algorithm used for classification tasks. 
In this case, the model is designed to classify iris flowers into different species based on the features provided in the dataset. 

The implementation builds the decision tree recursively by finding the best feature and threshold for splitting the data at each node. 
The tree is constructed until a stopping criterion, such as reaching a maximum depth or achieving pure leaf nodes (homogeneous class labels), is met.

## Iris Dataset
The Iris dataset is a common dataset used in machine learning, and it can be obtained from various sources, such as scikit-learn's datasets module. 

The dataset includes four features for each iris sample: sepal length, sepal width, petal length, and petal width. 

The corresponding target variable represents the species of the iris flower (setosa, versicolor, or virginica).

The code demonstrates the implementation of a decision tree classifier without relying on external machine learning libraries, offering insights into the fundamental concepts of decision tree construction. 

While this implementation serves as a basic introduction, for practical use, it's recommended to leverage well-established machine learning libraries like scikit-learn, which provide optimized and feature-rich implementations of decision trees and other classifiers.

## Recording Link
[link](https://drive.google.com/drive/folders/1j8dxdIk-yS2lx3HewK9ifiThJKBI-gxM?usp=sharing)

# Requirements
The provided code requires the following libraries:
1. **NumPy**: NumPy is used for numerical operations and array manipulations. It is a fundamental library for scientific computing with Python.
2. **scikit-learn**: Although not used in the core decision tree implementation, scikit-learn is a popular machine learning library that provides the Iris dataset and is used for splitting the dataset into training and testing sets, as well as evaluating the accuracy of the model.

    ## Installation
    ```bash
    pip install numpy
    pip install scikit-learn  
    ```
