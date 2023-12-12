#CG
To verify whether a given sequence of points \( P = \langle p_1, p_2, \ldots, p_n \rangle \) represents the vertices of a convex polygon in counter-clockwise order, you can use the following algorithm. The idea is to check if all consecutive triplets of points make left turns, indicating a counter-clockwise order.

```python
# Given three points, return True if they make a counter-clockwise turn.
def is_ccw(p1, p2, p3):
    cross_product = (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1])
    return cross_product > 0

def verify_convex_polygon(P):
    n = len(P)

    if n < 3:
        return False

    # Check the orientation of consecutive triplets of points
    for i in range(n - 2):
        if not is_ccw(P[i], P[i + 1], P[i + 2]):
            return False

    # Check the last triplet of points (n-2, n-1, 0)
    if not is_ccw(P[n - 2], P[n - 1], P[0]):
        return False

    # Check the first triplet of points (n-1, 0, 1)
    if not is_ccw(P[n - 1], P[0], P[1]):
        return False
    return True

if __name__ == "__main__":
	P = [(0, 0), (1, 1), (2, 0), (1, -1)]
	result = verify_convex_polygon(P)
	print(result)
```

In this algorithm, `is_ccw` checks whether three points make a counter-clockwise turn using the cross product. The `verify_convex_polygon` function then iterates through all consecutive triplets of points and checks their orientation. If all triplets make counter-clockwise turns, the sequence \( P \) represents a convex polygon in counter-clockwise order.

## Time Complexity
-----
The time complexity of the provided algorithm is \(O(n)\), where \(n\) is the number of points in the input sequence \(P\).

The primary reason for the linear time complexity is the single loop that iterates through all consecutive triplets of points. In each iteration, constant-time operations are performed to check whether the triplet forms a counter-clockwise turn. 
Therefore, the overall time complexity is proportional to the number of points in the input sequence, making it an efficient algorithm for verifying convex polygons in counter-clockwise order.

To run the algorithm and visualize the points on a 2-dimensional space, we can use a simple Python script along with the `matplotlib` library. Below is an example script that incorporates the verification algorithm and plots the points:

```python
import matplotlib.pyplot as plt

def is_ccw(p1, p2, p3):
    cross_product = (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1])
    return cross_product > 0

def verify_convex_polygon(P):
    n = len(P)

    if n < 3:
        return False

    for i in range(n - 2):
        if not is_ccw(P[i], P[i + 1], P[i + 2]):
            return False

    if not is_ccw(P[n - 2], P[n - 1], P[0]):
        return False

    if not is_ccw(P[n - 1], P[0], P[1]):
        return False

    return True

if __name__ == "__main__":
	points = [(0, 0), (1, 1), (2, 0), (1, -1)]
	is_convex_polygon = verify_convex_polygon(points)
	# Plot the points and connect them if they form a convex polygon
	x, y = zip(*points)
	plt.scatter(x, y, color='blue')

	if is_convex_polygon:
	    # If the points form a convex polygon, connect them in order
	    points.append(points[0])  
	    # Connect the last point to the first to close the polygon
	    plt.plot(*zip(*points), color='green')

	plt.title('Convex Polygon Verification')
	plt.xlabel('X-axis')
	plt.ylabel('Y-axis')
	plt.grid(True)
	plt.show()
```
This script uses `matplotlib` to create a scatter plot of the given points. If the points form a convex polygon, the script also connects them in order to visualize the polygon in green. 
![[convex-verification.png]]