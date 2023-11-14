Good solutions to algorithmic problems of a geometric nature are mostly based on two ingredients.
One is a through understanding of the geometric properties of the problem, the other is a proper application of algorithmic techniques and data structures.

## Convex Definition
---------------------------------
A subset S of the plane is called *convex* if and only if for any pair of points the line segment is completely contained in S.

## Convex Hull Definition
---------------------------------
The *convex hull* of a set S, is the smallest convex set that contains S.


## How do we compute the convex hull?
Before we can answer this question we must ask another question.
What does it mean to compute the convex hull?

The convex hull of ***P*** is a convex polygon.
A natural way to represent a polygon is by listing its vertices in clockwise order, starting with an arbitrary one.

The first definition of convex hulls is of little help when we want to design an algorithm to compute the convex hull. 
It talks about the intersection of all convex sets containing P, of which there are infinitely many.
The observation that ***CH(P)*** is a convex polygon is more useful.
Let's see what the edges of ***CH(P)*** are.

Both end points *p* and *q* of such an edge are points of *P*, and if we direct the line through *p* and *q* such that **CH(P)*** lies to the right, then all the points of *P* must lie to the right of this line.
The reverse is also true: If all points of *P | {p,q}* lie to the right of the directed line through *p* and *q*, the pq is an edge of ***CH(P)***.


## Algorithm SlowConvexHull(P)
------
*Input*. A set *P* of points in the plane.
*Output*. A list *L* containing the vertices of ***CH(P)*** in clockwise order.

Analyzing the time complexity of SlowConvexHull is easy.
we check *n^2 - n* pairs of points. For each pair we look at the *n - 2* other points to see whether they all lie on the right side.
This will take *O(n^3)* time in total.

An algorithm with a cubic running time is too slow to be of practical use for anything but the smallest input sets.

We have been a bit careless when deriving the criterion of when a pair *p, q* defines an edge of ***CH(P)***.
A point *r* does not always lie to the right or to the left of the line through *p* and *q*, it can also happen that it lies ***on*** this line.
What should we do then?
This is what we call a *degenerate case*, or a *degeneracy* for short.

We have been ignoring another important issue that can influence the correctness of the result of our algorithm.
Although we have proven the algorithm to be correct and to handle all special cases, it is not robust: small errors in the computations can make it fail in completely unexpected ways. 
The problem is that we have proven the correctness assuming that we can compute exactly with real numbers.

To this end we apply a standard algorithm design technique: we will develop an *incremental algorithm*. This means that we will add the points in *P* one by one, updating our solution after each addition.
We give this incremental approach a geometric flavor by adding the points form left to right.
So we first sort the points by x-coordinate, obtaining a sorted sequence *P1,...,Pn*, and then we add them in that order.

Because we are working from left to right, it would be convenient if the convex hull vertices were also ordered from left to right as they occur along the boundary. BUT this is not the case.
Therefor we first compute only those convex hull vertices that lie on the *upper hull*, which is the part of the convex hull running from the leftmost point *P1* to the rightmost point *Pn* when the vertices are listed in clockwise order.
In other words, the upper hull contains the convex hull edges bounding the convex hull from above.
In a second scan, which is performed from right to left, we compute the remaining part of the convex hull, the *lower* hull.