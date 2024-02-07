### Code Documentation

#### `set_array(input_data)`

This function takes a 2D array (`input_data`) as input, where each row represents an instance of data with the last element being the class label. It returns an array of dictionaries (`array`), where each dictionary represents a unique attribute (column) in the dataset. The keys of the dictionary are unique values in that attribute, and the values are lists containing counts of occurrences of class labels `'recurrence-events'` and `'no-recurrence-events'`.

**Parameters:**
- `input_data`: A 2D array representing the dataset.

**Return:**
- `array`: A list of dictionaries, where each dictionary represents a unique attribute in the dataset.

#### `get_prob(input_data, array)`

This function calculates and returns the probability of each class (`'recurrence-events'` and `'no-recurrence-events'`) given the training data and attribute dictionary.

**Parameters:**
- `input_data`: A 2D array representing the training dataset.
- `array`: A list of dictionaries representing attributes and their counts.

**Return:**
- `array`: The modified array where the values are the probabilities of each class for each attribute.
- `prob_class1`: Probability of class `'recurrence-events'`.
- `prob_class2`: Probability of class `'no-recurrence-events'`.

#### `test(data, array, p_class1, p_class2)`

This function tests the classifier's accuracy on a test dataset and returns the accuracy percentage.

**Parameters:**
- `data`: A 2D array representing the test dataset.
- `array`: The array of attribute dictionaries.
- `p_class1`: Probability of class `'recurrence-events'`.
- `p_class2`: Probability of class `'no-recurrence-events'`.

**Return:**
- Accuracy percentage: The percentage of correctly classified instances in the test dataset.

#### Example of Usage:

```python
with open("Breast_Cancer_dataset_2.txt", "r") as file:
    lines = file.readlines()
    l = [0 for i in range(len(lines))]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            l[i] = lines[i].strip().split(",")

input_data = l[0:167]
input_test = l[167:]
a_new = set_array(input_data)
print(a_new)
f_arr, prob1, prob2 = get_prob(input_data, a_new)
print(f_arr)
print(prob1)
print(prob2)
print(test(input_test, f_arr, prob1, prob2))
```

This example demonstrates how to read a dataset, create the attribute array, compute class probabilities, and test the Naive Bayes classifier's accuracy on a separate test dataset.
