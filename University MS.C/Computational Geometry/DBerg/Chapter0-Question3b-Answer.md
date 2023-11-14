To find the largest axis-parallel square inside a convex polygon \( P \) with \( n \) vertices, you can use a binary search approach to efficiently determine the maximum side length of the square. Here's a high-level outline of the algorithm:

1. **Preprocessing:**
   - Compute the bounding box of the convex polygon \( P \). This bounding box will be used as an initial guess for the maximum side length of the square.

2. **Binary Search:**
   - Perform a binary search on the side length of the square. The search space should be within the range [0, maxBoundingSideLength], where maxBoundingSideLength is the maximum side length that can fit inside the bounding box without intersecting the polygon.
   - For each iteration of the binary search, check if a square of the given side length can fit entirely inside the convex polygon. You can achieve this by checking if all four corners of the square are inside the convex polygon.

3. **Result:**
   - The final side length obtained from the binary search will be the largest axis-parallel square that fits entirely inside the convex polygon.

Here's a Python-like pseudocode for the algorithm:

```python
def largest_axis_parallel_square(convex_polygon):
    # Step 1: Compute bounding box
    min_x, min_y, max_x, max_y = compute_bounding_box(convex_polygon)
    max_bounding_side_length = min(max_x - min_x, max_y - min_y)

    # Step 2: Binary Search
    low, high = 0, max_bounding_side_length
    epsilon = 1e-6  # A small value for floating-point precision

    while high - low > epsilon:
        mid = (low + high) / 2

        # Check if square of side length mid can fit inside the convex polygon
        if can_fit_square_inside(convex_polygon, mid):
            low = mid
        else:
            high = mid

    # Step 3: Result
    return low

# Helper functions
def compute_bounding_box(convex_polygon):
    # Calculate the bounding box of the convex polygon
    # Return min_x, min_y, max_x, max_y

def can_fit_square_inside(convex_polygon, side_length):
    # Check if a square of the given side length can fit entirely inside the convex polygon
    # Check if all four corners of the square are inside the convex polygon
```

Note: The implementation of `compute_bounding_box` and `can_fit_square_inside` will depend on the representation of the convex polygon and the details of the geometric operations required. These functions involve basic geometric computations and checks. Additionally, you may need to handle special cases, such as when the convex polygon is too small to accommodate a square.

This algorithm has a time complexity of \(O(\log(\text{{maxBoundingSideLength}}))\) due to the binary search. The geometric checks within the binary search are generally efficient and can be done in \(O(n)\) time, where \(n\) is the number of vertices in the convex polygon.