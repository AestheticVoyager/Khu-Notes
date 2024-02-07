# Incremental Convex Hull(2D)
Simple implementation of the incremental algorithm for computing the convex hull of a set of 2D points. Here's a breakdown of the code:

1. **Point Class:**
   - `Point` class represents a 2D point with `x` and `y` coordinates.

2. **Quicksort Function:**
   - `quicksort` is a generic quicksort implementation that sorts a list of objects based on a specified attribute (`attr`).
   - It uses the attribute values for comparison during the sorting process.

3. **Right Turn Function:**
   - `right_turn` determines if three points (p1, p2, p3) make a right turn or not.
   - It calculates the cross product and checks if it is negative, indicating a right turn.

4. **Incremental Convex Hull Function:**
   - `incremental_convex_hull` computes the convex hull of a set of points using the incremental algorithm.
   - It sorts the points based on their x-coordinates.
   - It then builds the upper and lower convex hulls separately, combining them at the end.

5. **Plot Polygon Function:**
   - `plot_polygon` is a utility function to visualize the convex hull and the original points using Matplotlib.

6. **Example Usage:**
   - An example set of points is created.
   - The convex hull is computed using the `incremental_convex_hull` function.
   - The convex hull and original points are plotted using `plot_polygon`.

7. **Example Output:**
   - The convex hull coordinates are printed.
   - A plot is generated with the convex hull and points.

**Note**: The incremental convex hull algorithm is an efficient way to compute the convex hull of a set of points in a dynamic setting, where points are added incrementally. 