#CG
# Line Segment Intersection for Map Overlay

## Map Layers
In a geographic information system (GIS) data is stored in separate layers.

A layer stores the geometric information about some theme, like land cover, road network, municipality boundaries, red fox habitat, ...

Map overlay is the combination of two (or more) map layers.
It is needed to answer questions like:
- What is the total length of roads through forests?
- What is the total area of corn fields within 1 km from a river?
- What area of all lakes occurs at the geological soil type "rock"?

To solve map overlay questions, we need (at the least) intersection points from two sets of line segments (possibly, boundaries of regions)

## The (Easy) Problem
Let's first look at the easiest version of the problem:
Given a set of *n* line segments in the plane, find all intersection points efficiently.

Input. A set *S* of line segments in the plane.
Output. The set of intersection points among the segments in *S*.
```
for each pair of line segments ei, ej ∈ S
	do if ei and ej intersect
		then report their intersection point
```
**Question:** Why can we say that this algorithm is optimal?
**Answer**: the asymptotic running time of an algorithm is always input-sensitive (depends on *n*)
We may also want the running time to be output-sensitive

----
**Question**: How many intersection points do we typically expect in our application?
**Answer**: If this number is *k*, and if *k*=*O(n)*, it would be nice if the algorithm runs in *O(n*log*n*) time.

## Plane Sweep
The **Plane Sweep Technique**: Imagine a horizontal line passing over the plane from top to bottom, solving the problem as it moves.
- The sweep line stops and the algorithm computes at certain positions => **events**
- The algorithm stores the relevant situation at the current position of the sweep line => **status**
- The algorithm knows everything it needs to know above the sweep line, and found all intersection points

## Status and Events
The **status** of this particular plane sweep algorithm, at the current position of the sweep line, is the set of line segments intersecting the sweep line, ordered from left to right.

The **events** occur when the status changes, and when output is generated.
`event = interesting y-coordinate`

## The events
When do the events happen? When the sweep line is at:
- an upper endpoint of a line segment
- a lower endpoint of a line segment
- an intersection point of a line segment
At each type, the **status** changes; at the third type **output** is found too

## Assume no degenerate cases
We will at first exclude degenerate cases:
- No two endpoints have the same y-coordinate
- No more than two line segments intersect in a point
- ...

## Even List and Status Structure
The **event list** is an abstract data structure that stores all events in the order in which they occur.
The **status structure** is an abstract data structure that maintains the current status.

## Status Structure
We use a balanced binary search tree with the line segments in the leaves as the **status structure**

**Sweep line reaches lower endpoint of a line segment**: delete from the status structure.
**Sweep line reaches intersection point**: swap two leaves in the status structure (and update information on the search paths)

## Finding Events
Before the sweep line algorithm starts, we know all **upper endpoint events** and all **lower endpoint events**

But: How do we know **intersection point events**???
**Recall**: Two line segments can only intersect if they are horizontal neighbors

`Algorithm FindIntersections(S)`
Input. A set of *S* of line segments in the plane.
Output. The intersection points of the segments in *S*, with for each intersection point the segments that contain it.
```
1. Initialize an empty event queue Q.
   Insert the segment endpoints into Q;
   When an upper endpoint is inserted, the corresponding segment should be stored with it.
2. Initialize an empty status structure T.
3. while Q is not empty
	do Determine next event point p in Q and delete it
		 HandleEventPoint(p)
```
----
## Event Handling
### 1. If the even is an **upper endpoint** event, and *s* is the line segment that starts at *p*:
1. Search with *p* in **T**, and insert *s* .
2. If *s* intersects its left neighbor in **T**, then determine the intersection point and insert in *Q* .
3. If *s* intersects its right neighbor in **T**, then determine the intersection point and insert in *Q* .

### 2. If the event is a lower endpoint event, and s is the line segment that ends at p:
1. Search with *p* in **T**, and delete *s* .
2. Let *sl* and *sr* be the left and right neighbors of *s* in **T** (before deletion).
3. If they intersect below the sweep line, then insert their intersection point as an event in *Q*

### 3. If the event is an intersection point event where *s* and *s'** intersect at *p*:
1. Exchange *s* and *s'* in **T**
2. If *s'* and its new left neighbor in **T** intersect below the sweep line, then insert this intersection point in *Q*
3. If *s* and its new right neighbor in *T* intersect below the sweep line, then insert this intersection point in *Q* .
4. Report the intersection point.
----
## Efficiency
How much time to handle an event?
At most one search in *T* and/or one insertion, deletion, or swap
At most twice finding a neighbor in *T*
At most one deletion from and two insertions in *Q*
Since *T* and *Q* are balanced binary search trees, handling an event takes only *O(logn)*  time

How many events?
- *2n* for the upper and lower endpoints
- *k* for the intersection points, if there are *k* of them

**In total**: *O(n+k)* events

Initialization takes O(*n*log*n*) time (to put all upper and lower endpoints events in *Q*)
Each of the O(*n+k*) events takes O(log*n*)
The algorithm takes O(*n*log*n*+*k*log*n*) time
if *k* = *O(n)*, then this is O(*n*log*n*)

**Note** that if *k* is really large, the brute force O(n^2) time algorithm is more efficient

---
## Degenerate Cases

How we deal with degenerate cases?
For two different events with the same y-coordinate, we treat them from left to right ⇒ the “upper” endpoint of a horizontal line segment is its left endpoint

How about multiply coinciding event points?
Let U(p) and L(p) be the line segments that have p as upper and lower endpoint, and C(p) the ones that contain p

**Question**: How do we handle this multi-event?

How efficient is a multiply coinciding event point handled? 
If |U(p)| + |L(p)| + |C(p)| = m, then the event takes
O(*m*log*n*) time.

What do we report?
- The intersection point itself
- Every pair of intersecting line segments
- The intersection point and every line segment involved
⇒ the output size for this one event is then O(1), O(m^2), or O(m), respectively
----
## Result
For any set of n line segments in the plane, all I intersections can be computed in O(*n*log*n*+*I*log*n*) time, and within this time bound, we can report for every intersection which line segments are involved.

----
## Conclusion
For every sweep algorithm:
- Define the status
- Choose the status structure and the event list
- Figure how events must be handled (with sketches!)
- To analyze, determine the number of events and how much time they take
Then deal with degeneracies.