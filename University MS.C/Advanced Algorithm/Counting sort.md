**Counting Sort** is a **non-comparison-based** sorting algorithm that works well when there is limited range of input values. 
It is particularly efficient when the range of input values is small compared to the number of elements to be sorted. 
The basic idea behind **Counting Sort** is to count the **frequency** of each distinct element in the input array and use that information to place the elements in their correct sorted positions.

```python
def count_sort(input_array):

    # Finding the maximum element of input_array.
    M = max(input_array)

    # Initializing count_array with 0
    count_array = [0] * (M + 1)

    # Mapping each element of input_array as an index of count_array
    for num in input_array:
        count_array[num] += 1

    # Calculating prefix sum at every index of count_array
    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]

    # Creating output_array from count_array
    output_array = [0] * len(input_array)
    for i in range(len(input_array) - 1, -1, -1):
        output_array[count_array[input_array[i]] - 1] = input_array[i]
        count_array[input_array[i]] -= 1
    return output_array

# Driver code
if __name__ == "__main__":
    # Input array
    input_array = [4, 3, 12, 1, 5, 5, 3, 9]
    # Output array
    output_array = count_sort(input_array)
    for num in output_array:
        print(num, end=" ")
```
