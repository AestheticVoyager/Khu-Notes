#CG
# Introduction
In the 1970s the field of computational geometry emerged, dealing with such geometric problems.
- Overlaying two maps is one the basic operations of geographic information System (GIS)
- Motion Planning problem (Crucial in robotics)
- Subdivision of a campus (Voronoi Diagram)

# Convex Hulls
## Definition of Plane and Space
- Plane (two-dimensional), R^2
- Space (three-dimensional), R^3
- Space (higher-dimensional), R^d

## Point Definition in Plane and Space
A point in the plane: P=(Px,Py)
A point in 3-dimensional space: P=(Px,Py,Pz)
A point in higher-dimensional space:P=(P1,P2,P3,...,Pd)

## Line
A line in the plane: y=mx+c

## Half-Plane
A half-plane in the plane: y <=mx+c OR y>=mx+c

## Description Size
- A simple polygon in the plane can be represented using 2n reals if it has *n* vertices (and necessarily, *n* edges)
- A set of *n* points requires *2n* reals
- A set of *n* line segments requires *4n* reals
- A point, line, circle, ... requires O(1), or constant, storage.
- A simply polygon with *n* vertices requires *O(n)*, or linear, storage.
- Any computation (distance, intersection) on two objects of *O(1)* description size takes *O(1)* time.
- A set of *n* real numbers can be sorted in O(*n*log*n*) time.
- A set of *n* real numbers can be stored in a data structure that uses O(*n*) storage and that allows searching, insertion, and deletion in O(*n*log*n*) time per operation.

## Convexity
A shape or set is **Convex** if for any two points that are part of the shape, the whole connecting line segment is also part of the shape.

## Convex Hull
For any subset of the plane(set of points, rectangle, simple polygon), its **convex hull** is the smallest convex set that contains that subset

## Convex Hull Problem
Give an algorithm that computes the convex hull of any given set of *n* points in the plane efficiently.
The input has 2*n* coordinates, so *O(n)* size.

## Algorithm Analysis & Correctness
Algorithm analysis generally has two components:
- Proof of correctness
- Efficiency analysis, proof of running time
- Are the general observations on which the algorithm is based correct?
- Does the algorithm handle **degenerate cases** correctly?

## Efficiency
Calculating the time complexity of the algorithm.
For example:
The sorting step takes O(*n*log*n*) time.
Adding a point takes O(*1*) time for the adding-part.
Removing points takes constant time for each removed point.
If due to an addition, *k* points are removed, the step takes O(*1+k*) time 

## Final Result
The convex hull of a set of *n* points in the plane can be computed in O(*n*log*n*) time, and this is optimal.

## Convex Hulls in 3D
For a 3-dimensional point set, the convex hull is a convex polyhedron.

The boundary is a planar graph, so it has O(*n*) vertices, edges and facets.


## Some other algorithms for constructing Convex Hulls

### Gift-Wrapping Algorithm
1. Start at lowest point
2. Rotate the line until we hit another point
	- All other points will lie on one side of this line
	- Look for the point that gives you the largest angle with the current line
3. Repeat
4. You're done when you get back to the starting point.

## Vectors
Let's talk about 2D vectors
A vector v=(x,y) is an "arrow" with a direction and length
Similar to a 2D point.

length of **v**: ||v||
||v|| = √x^2 + y^2

Direction of **v**:
ø = atan(y/x)

**v+u** = (Vx + Ux, Vy + Uy)

We can also "multiply" two vectors:
- Dot product: V.U=VxUx + VyUy
- Useful fact: V.U = ||V|| ||U||cosø -> cosø = (V.U) / (||V|| ||U||)

## Back to the Convex Hull and Gift Wrapping Algo
What is the running time of this algorithm?

**O(nh)**
**n** = number of points
**h** = number of convex hull verices
**O(n^2)** in WORST Case


## Graham Scan Method
- Form a simple polygon(connect the dots as before)
- Remove points at concave angles (one at a time, backtracking one step when any point is removed).
- Continue until you get all the way around.
Start with the lowest pint(anchor point)
## Graham Scan: Phase 1
Now, form a closed simple path traversing the points by increasing angle with respect to the anchor point
## Graham Scan: Phase 2
The anchor point and the next point on the path must be on the hull
Keep the path and the hull points in two sequences:
- Elements are removed from the beginning of the path sequence and are inserted and deleted from the end of the hull sequence
Orientation is used to decide whether to accept or reject the next point

## Time Complexity of Graham Scan
**Phase 1** -> O(*n*log*n*)
	points are sorted by angle around the anchor
**Phase 2** -> O(*n*)
	each point is inserted into the sequence exactly once, and each point is removed from the sequence at most once
**Total Time Complexity** -> O(*n*log*n*)

## Recursion Time Complexity Calculation
T(n) = { O(1) if n = 1;
			{ 2T(n/2) + O(n) if n > 1.

NOTE: Image slide 35 of 40 in file CH 1-Slides 3.pdf


## Algorithm Summary
| Algorithm | Speed | 
| ---- | ---- |
| Brute Force | O(*n*^3) |
| Gift wrapping | O(*n*h) |
| Graham Scan | O(*n*log*n*) |
| Jarvis's March | O(*n*h) |
| QuickHull | O(*n*h) |
| Divide-and-Conquer | O(*n*log*n*)|
| Monotone chain | O(*n*log*n*)|
| Incremental | O(*n*log*n*)|
| Marriage-before-Conquest | O(*n*logh)|

