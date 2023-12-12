# Subdivision representation and map overlay

**map overlay** is the combination of two or more map layers.
It is needed to answer questions like:
- What is the total length of roads through forests?
- What is total area of corn fields within 1 km from a river?
- What area of all lakes occurs at the geological soil type "rock"?

To solve map overlay questions, we need (at least) intersection points from two sets of line segments (possibly, boundaries of regions)

To solve map overlay questions, we also need to be able to represent subdivisions.

A planar subdivision is a structure induced by a set of line segments in the plane that can only intersect at common endpoints. It consists of vertices, edges, and faces.

## Subdivisions
### Vertices
are the endpoints of the line segments.

### Edges
are the interiors of the line segments.

### Faces
are the interiors of connected two-dimensional regions that do not contain any point of any line segment.

----
Objects of the same dimensionality are adjacent or not; objects of different dimensionality are incident or not.

Any face has zero or more inner boundaries.

Vertices, edges, and faces form a partition of the plane.

If a planar subdivision is induced by n line segments, it has exactly n edges, and at most 2n vertices

**Question:** And how many faces?
**Answer:** Every face is bounded by at least 3 edges, and every edge bounds at most 2 faces => 2n/3=O(n)

----
## Euler's Formula for planar Graphs
If S is the planar subdivision with V vertices, E edges, and F faces, then
`V-E+F ≥ 2`
with equality if the vertices and edges of S form a connected set.

Example:
V=9
E=10
F=4
V-E+F=3

Another example:
V=11
E=12
F=4
V-E+F=2

----
## Representing subdivisions
A subdivision representation has a vertex-object class, an edge-object class, and a face-object class.
It is a pointer structure where objects can reach incident (or adjacent) objects easily.

----
## Half Edges
We apply a trick/hack/impossibility:
split every edge length-wise(!) into two half-edges

Every half-edge:
- Has exactly one half-edge as its twin
- is directed opposite to its Twin
- is incident to only one face (left)

----
## The doubly-connected edge list
The **doubly-connected edge list** is a subdivision representation structure with an object for every vertex, every half-edge, and every face
A vertex object stores:
- Coordinates
- IncidentEdge (some half-edge leaving it)

A half-edge object stores:
- **Origin** (vertex)
- **Twin** (half-edge)
- **IncidentFace** (face)
- **Next** (half-edge in cycle of the incident face)
- **Prev** (half-edge in cycle of the incident face)

A face object stores:
- **OuterComponent** (half-edge of outer cycle)
- **InnerComponent** (list of half-edges for the inner cycles bounding the face)

----
## Face Information
- Determine all cycles of half-edges, and whether they are inner or outer boundaries of the incident face
- Make a face object for each outer boundary, plus one for the unbounded face, and set the **OuterComponent** variable of each face. Set the **incidentFace** variable for every half-edge in an outer boundary cycle.
- Determine the leftmost vertex of each inner boundary cycle
- For all of these leftmost vertices, determine the edge horizontally left of it, take the downward half-edge of it, and its cycle (by plane sweep) to set **InnerComponents** for all faces and **IncidentFace** for half-edges in inner boundary cycles.

----
##  Efficiency
Every event takes *O*(log*n*) or *O*(*m*+log*n*) time to handle where *m* is the sum of the degrees of any vertex from S1 and/or S2 involved.

The sum of the degrees of all vertices is exactly twice the number of edges in the output

**Theorem**: Given two planar subdivisions S1 and S2, their overlay can be computed in *O*(*n*log*n*+*k*log*n*) time, where *k* is the number of vertices of the overlay.