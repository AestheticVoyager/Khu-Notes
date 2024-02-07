# Segment Intersection
This code is designed to work with 2D geometric objects, specifically points and line segments. Let's break down the main components and functionality:

1. **Point Class:**
   - Represents a point in a 2D space with `x` and `y` coordinates.
   - Used to define the endpoints of line segments.

2. **Segment Class:**
   - Represents a line segment by storing its starting (`start`) and ending (`end`) points.
   - Provides methods:
     - `upper_endpoint`: Returns the endpoint with the higher `y` coordinate.
     - `intersects`: Checks if the current segment intersects with another segment.
     - `segment_intersection` (staticmethod): Determines the intersection point of two line segments.

3. **find_intersections Function:**
   - Takes a list of line segments as input.
   - Uses combinations of segments to find all intersections.
   - Utilizes the `intersects` method from the `Segment` class.

4. **visualize_segments_intersections Function:**
   - Takes a list of line segments and a list of intersection points as input.
   - Uses Matplotlib to create a plot:
     - Blue lines represent the input line segments.
     - Red dots indicate intersection points.

5. **Main Block:**
   - Creates instances of points and segments to define three line segments.
   - Calls `find_intersections` to identify intersections among the segments.
   - Calls `visualize_segments_intersections` to generate a plot visualizing the segments and their intersections.

Overall, the code provides a way to work with geometric entities, check for intersections among line segments, and visualize the results. 
The example in the main block demonstrates the usage by defining three line segments and displaying their intersections on a plot using Matplotlib.