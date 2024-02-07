# 4023131508 Mahan Fallah
from sklearn.neighbors import KNeighborsClassifier

def leave_one_out_cross_validation(classifier, features, labels):
    n = len(features)
    total_accuracy = 0.0

    for i in range(n):
        test_features, test_label = features[i], labels[i]
        train_features = features[:i] + features[i+1:]
        train_labels = labels[:i] + labels[i+1:]

        classifier.fit(train_features, train_labels)
        prediction = classifier.predict([test_features])[0]
        total_accuracy += 1 if prediction == test_label else 0

    avg_accuracy = total_accuracy / n
    return avg_accuracy

# Input data
red = [(1, 6), (2, 7), (3, 8), (4, 9), (7, 3), (8, 4)]
blue = [(2, 6), (3, 7), (6, 1), (7, 2), (8, 3), (9, 4)]
features = red + blue
labels = [0] * len(red) + [1] * len(blue)  # 0 for red, 1 for blue

best_k = None
max_accuracy = 0.0

for k in range(1, 11):  # You can adjust the range based on your preference
    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    accuracy = leave_one_out_cross_validation(knn_classifier, features, labels)

    # Update the best K if the current K has a higher accuracy
    if accuracy > max_accuracy:
        max_accuracy = accuracy
        best_k = k

print(f"Optimal value of K: {best_k}")
print(f"Accuracy for the optimal K: {max_accuracy}")
print(f"Error rate for the optimal K: {1 - max_accuracy}")
