#CG 
# Triangulating a polygon in O(n log*n)
In 1991, Seidel found a practical algorithm for triangulating polygons with an expected running time of O (n log*n). 
The algorithm can triangulate any set of overlapping and self-intersecting polygons and lines in the plane with near-linear expected time.
Its virtues lie in its simplicity.
It uses no divide-and-conquer or recursion and no “Jordan Sorting”.
Its expected performance admits a very straightforward and self-contained analysis.
Finally, it is practical and relatively simple to implement, a property that very few, if any, of the algorithms mentioned can claim.

It should also be mentioned that in 2000 Amato et al.
found a similar linear algorithm with far less overhead than Chazelle’s, by using randomization as in Seidel’s algorithm. This would still be a formidable job to implement with all its details.

## Seidels Algorithm
1. Trapezoidal decomposition or trapezoidation
2. Generation of monotone mountains
3. Triangulating by ear clipping method

### 1 Trapezoidal decomposition or trapezoidation
A _trapezoidation_ is formed by extending a horizontal ray in each direction from every vertex, and stopping the ray as soon as it hits another edge.
This will divide the plane into regions by edges and rays, and each such region is a trapezoid.
A trapezoid has a horizontal upper and lower boundary, and an edge or a piece of an edge as a boundary on either side.
Either the upper or lower boundary may have zero length, in which case the trapezoid will be a triangle.
The set of trapezoids obtained in this manner is called a _trapezoidation_, and is unique for any given polygon.

![[Trapezoidal.png]]
Seidel’s algorithm is a randomized way of computing _trapezoidation_. This means that every edge is equally likely to be added in the _trapezoidation_. For this purpose a random sequence of edges is generated. This ensures that actual running time will not be significantly worse than expected running time.

_Trapezoidation_ routine starts with an empty plane and adds in edges one by one. 
The algorithm checks if endpoints of the edge are added to the _trapezoidation_ already.
Those which have not been added are added one by one.
This will divide the region (in which point is added) into two by means of horizontal rays starting from that point and extending in both directions (left & right).
Next the edge is added between two points.
This is done by starting from the top point and moving down one region at a time, until bottom point is reached.
For each region traversed in this manner, the region is divided in two by means of the new edge.
Whenever this causes two regions on top of each other to have same left and right hand boundary, these two regions are merged into one.
Each of the regions created in this manner will be a trapezoid.
Note that in doing this; we never need to explicitly calculate the intersections of edges and rays.

Each trapezoid will know which edges and rays it is bounded by. For this we will have a special memory structure which stores information about each trapezoid. This structure is explained as below.

### Trapezoid Data Structure
High - Upper vertex of the trapezoid

Low - Lower vertex of the trapezoid

U1, U2 - Upto two adjacent trapezoids above

D1, D2 - Upto two adjacent trapezoids below

U3 - Third extra region above (if any)

U3 SIDE - Determines whether the third extra region is towards left or right

LSEG, RSEG - Left and right edges of the trapezoid

SINK - Position of trapezoid in tree structure (discussed later)

STATE - Represents validity of trapezoid (Inside or outside)

The algorithm also needs to be able to efficiently tell where to place new points in the current _trapezoidation_. 
One way of doing this is by creating a tree lookup structure for trapezoids.
The tree starts only with a root representing the original empty plane and each time a region is split in two, the corresponding leaf in the tree is changed into a node with two children.
This new node can either be a vertex or an edge.
The two children represent two resulting trapezoids.
Thus each leaf in the tree represents a trapezoid (region) and each node in the tree represents either vertex or edge.
By querying whether the point we are adding is above or below a vertex in the tree, or to which side of an edge it is, we can traverse the tree to find the correct region in which the point will be added.
The tree is a strict binary tree and also called as “query structure”.
This tree structure is explained below:

### Query Structure
Node type - Whether the node in tree is vertex or edge or trapezoid

Segment number - Points to vertex or edge if node type is either vertex or edge

Trapezoid number - Points to trapezoid in trapezoid data structure if node type is trapezoid.

Left - Points to left child node

Right - Points to right child node

Parent - Points to parent node

### Steps for adding an edge in the trapezoidation are as follows:
1. Select an edge from randomly generated sequence of edges.
2. Find higher vertex of that edge.
3. Traverse the tree to find correct region in which higher vertex will be added.
	- If vertex is not already added, change the leaf node (trapezoid) into a vertex node. This node will have two trapezoids as its left and right children. Left child represents region below the vertex whereas right child represents region above the vertex. Right child trapezoid is old region to be split by the vertex. Left child trapezoid is new region introduced after addition of vertex. Update the trapezoid structure.
        - If vertex is already added (as part of previously added edge), just traverse the tree to find the region in which the vertex reside. This is required for addition of an edge. 
4. Add lower vertex to the _trapezoidation_ and follow the same procedure as for higher vertex to traverse the tree and find correct region.
5. Finally, add the edge starting from higher vertex to lower vertex. This edge will split all the regions which are below higher vertex and above lower vertex. Update the trapezoid structure, for regions split by the edge.

### 2 Generation of monotone mountains
Given the _trapezoidation_ of a polygon, a triangulation can be easily computed in linear time. Let us consider only those trapezoids that are inside the polygon, as these are the ones we will want to triangulate. Trapezoids which lie inside the polygon are found out using fill rule. Fill rule and it’s realization for triangulation is explained in section later below.


First of all, note that each trapezoid will be empty, i.e. there will be no vertices or edges inside it. Further note that the upper and lower boundaries of each trapezoid are created by the extension of rays from vertices, such that each trapezoid has one bounding upper and one bounding lower vertex. Lower is defined here lexicographically, i.e. of two vertices with the same y-coordinate; the rightmost will be considered lower. This is assumed for all vertices and it assures that no edge is being treated as if it was horizontal, and that no trapezoid will have more than one upper and one lower bounding vertex. In some cases the two bounding vertices will be on the same side of the trapezoid, and in other they may be on opposite sides, or in the middle. Whenever the two vertices are not along the same edge, one can draw a diagonal between them without intersecting any edges since each trapezoid is empty. Addition of these diagonals is illustrated in figure 4. Resulting polygons bounded by edges and diagonals are termed as _**monotone mountains**_**.**


Monotone mountains have one edge called the base, which extends from the uppermost point to the lowermost point. The rest of the vertices form what is called a monotone chain, which is characterized by the fact that traversing polygon from the top, every vertex will be lower than the previous one. If a monotone mountain is put with its base extending horizontally, it resembles a mountain range, hence its name.
![[Figure4.png]]

### 3 Triangulation by ear clipping method
If the inside angle between two edges of the polygon is less than л, the vertex is convex. 
If the triangle described by a convex vertex and its two neighbors contain no other vertices, the triangle is an ear of the polygon. 
Any convex vertex of the monotone chain is the tip of an ear, with the possible exception of the vertices of the base. 
Cutting such an ear off from a monotone mountain will always result in a smaller monotone mountain. 
This leads to a simple linear procedure for triangulating such polygons. Start with a list of all these convex vertices, and run through the list, cutting off each convex vertex and creating a triangle. 
For each vertex that is being cut, if its neighbors were not already convex, see if they have now become convex, and if either one has, add it to the end of the list. Once you have reached the end of the list, you are done. The algorithm is summarized in Table1.