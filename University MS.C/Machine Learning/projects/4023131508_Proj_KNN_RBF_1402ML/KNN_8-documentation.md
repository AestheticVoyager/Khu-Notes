# Optimal Value of K for KNN algorihtm
To find the optimal value of K for the KNN algorithm using Leave-One-Out Cross-Validation (LOOCV), you can iterate over different values of K and calculate the error rate for each K.
LOOCV involves using one data point as the test set and the remaining data points as the training set in each iteration.
The error rate is calculated based on how well the model predicts the left-out data point.

## Leave-One-Out Cross-Validation
Leave-One-Out Cross-Validation (LOOCV) is a technique used to assess the performance of a machine learning model while maximizing the use of available data.
The process involves systematically leaving out one data point from the dataset as the test set and training the model on the remaining n-1 data points.
This procedure is repeated n times, where n is the total number of data points, with each iteration using a different data point as the test set.
The model's performance is then evaluated by calculating the average error or accuracy across all iterations.
LOOCV is particularly useful when dealing with small datasets, as it provides a rigorous assessment of a model's generalization ability and helps mitigate issues related to overfitting or underfitting.

## Advantage of LOOVC
The advantage of LOOCV lies in its exhaustive use of available data for both training and testing, making it a robust evaluation method.
However, this approach can be computationally expensive, especially for large datasets, as it requires fitting the model multiple times.
Despite its computational cost, LOOCV is widely employed in situations where maximizing data utilization and obtaining an unbiased estimate of model performance are critical considerations.

## Python snippet without scikit-learn
Here's a simpler Python code snippet for Leave-One-Out Cross-Validation (LOOCV) without using external libraries like scikit-learn:

```python
# Given data
data = [(1, 6, 0), (2, 7, 0), (3, 8, 0), (4, 9, 0), (7, 3, 1), (8, 4, 1), (2, 6, 1), (3, 7, 1), (6, 1, 1), (7, 2, 1), (8, 3, 1), (9, 4, 1)]

# Iterate over different values of K
best_k = None
min_error_rate = float('inf')

for k in range(1, 11):  # You can adjust the range based on your preference
    error_rates = []

    # Perform LOOCV
    for i in range(len(data)):
        # Use one data point as the test set
        test_point = data[i]
        train_data = data[:i] + data[i+1:]

        # Separate features and labels
        X_train = [(x, y) for x, y, _ in train_data]
        y_train = [label for _, _, label in train_data]

        # Train the model
        # For simplicity, this example uses Euclidean distance to find neighbors
        neighbors = sorted(train_data, key=lambda point: ((point[0] - test_point[0])**2 + (point[1] - test_point[1])**2)**0.5)[:k]

        # Make a prediction based on the majority class of neighbors
        prediction = max(set([label for _, _, label in neighbors]), key=[label for _, _, label in neighbors].count)

        # Calculate error rate
        error_rates.append(0 if prediction == test_point[2] else 1)

    # Calculate mean error rate for the current K
    mean_error_rate = sum(error_rates) / len(error_rates)

    # Update the best K if the current K has a lower error rate
    if mean_error_rate < min_error_rate:
        min_error_rate = mean_error_rate
        best_k = k

print(f"Optimal value of K: {best_k}")
print(f"Error rate for the optimal K: {min_error_rate}")
```
