
# Triangulating a simple polygon in linear time
[**Bernard Chazelle**](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjUuZyBn7WCAxWFxgIHHWENB70QFnoECCIQAQ&url=https%3A%2F%2Fwww.cs.princeton.edu%2F~chazelle%2F&usg=AOvVaw21UQXRvLZSKJswAcOV4wW5&opi=89978449)

## Abstract
We give a deterministic algorithm for triangulating a simple polygon in linear time.
The basic strategy is to build a coarse approximation of a triangulation in a bottom-up phase and then use the information computed along the way to refine the triangulation in a top-down phase.
The main tools used are the [polygon-cutting theorem](https://www.cs.princeton.edu/techreports/1990/264.pdf), which provides use with a balancing scheme, and the planar separator theorem, whose role is essential in the discovery of new diagonals.
Only elementary data structures are required by the algorithm. In particular, no dynamic search trees, finger trees, or point-location structures are needed.

## Introduction
### What is [triangulation](https://en.wikipedia.org/wiki/Polygon_triangulation)?
Recall that to triangulate a polygon is to subdivide it into triangles without adding any new vertices.

### Triangulation algorithms history and breakthroughs
Triangulating a simple polygon has been one of the most outstanding open problems in two-dimensional computational geometry.

It is a basic primitive in computer graphics and, generally, seems the natural preprocessing step for most nontrivial operations on simple polygons.

Despite its apparent simplicity, however, the triangulation problem has remained elusive.

In 1978 **Garey**, gave an **O(n log n)** time algorithm for triangulating simple n-gon.

While it was widely believed that triangulating should be easier than sorting, no proof was to be found until 1986, when **[Tarjan](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi4vtzbn7WCAxXJKewKHSOhDusQFnoECCoQAQ&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FRobert_Tarjan&usg=AOvVaw1FfBENPg9_DplxnQ9ArVTr&opi=89978449)** and **Van Wyk** discovered an **O(n loglog n)** algorithm.

Following this breakthrough, **Clarkson** discovered a [*Las Vegas* algorithm](https://en.wikipedia.org/wiki/Las_Vegas_algorithm), recently simplified by **Seidel** with **O(n log* n)** expected time.

In 1989 **[Kirkpatrick](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiRk6bLoLWCAxVHKewKHe3sDzMQFnoECEQQAQ&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FDonald_Kirkpatrick&usg=AOvVaw03d7VjhuE_kmmgxiwDdq1E&opi=89978449)** gave a new conceptually simpler **O(n log log n)** time algorithm, and they also derived an **O(n log* n)** bound for the case where vertices have polynomially bounded integer coordinates.

Other results on the triangulation problem include linear or quasi-linear algorithms for restricted classes of polygons.

[Bernard Chazelle](https://en.wikipedia.org/wiki/Bernard_Chazelle) showed in 1991 that any simple polygon can be triangulated in linear time, though the proposed algorithm is very complex.
A simpler randomized algorithm with linear expected time is also known.

The [time complexity](https://en.wikipedia.org/wiki/Time_complexity "Time complexity") of triangulation of an n-vertex polygon _with_ holes has an Ω(n log n) [lower bound](https://en.wikipedia.org/wiki/Lower_bound "Lower bound"), in algebraic [computation tree](https://en.wikipedia.org/wiki/Computation_tree "Computation tree") models of computation.

It is possible to compute the number of distinct triangulations of a simple polygon in polynomial time using [dynamic programming](https://en.wikipedia.org/wiki/Dynamic_programming "Dynamic programming"), and (based on this counting algorithm) to generate [uniformly random](https://en.wikipedia.org/wiki/Discrete_uniform_distribution "Discrete uniform distribution")triangulations in polynomial time.

However, counting the triangulations of a polygon with holes is [#P-complete](https://en.wikipedia.org/wiki/%E2%99%AFP-complete "♯P-complete"), making it unlikely that it can be done in polynomial time.

----
What makes fast polygon triangulation a difficult problem are the basic inadequacies of either a pure top-down or a pure bottom-up approach.

To proceed top-down is to look at the whole polygon and infer global information right away.

We can rely on the polygon-cutting theorem which says that the polygon can be cut along a diagonal into two roughly equal-size pieces.

The immediate dilemma is that to find such diagonal appears just as difficult as triangulating the whole polygon to begin with.

Besides, we would actually need to find such a diagonal in sub-linear amortized time to keep our hopes for an optimal triangulation algorithm alive.

A bottom-up approach, on the other hand, involves computing say, triangulations oof sub-pieces of the polygon’s boundary.

This suffers from the obvious flaw that too much information gets to be computed.

Indeed, diagonals for small pieces of the boundary are not guaranteed to be diagonals of the whole polygon and might therefore be wasted.

Our solution is to mix bottom-up and top-down approaches together.

The basic strategy is to build a coarse approximation of a triangulation in a bottom-up phase and then use the information computed along the way to refine the triangulation in a top-down phase.

The main tools used are:
1. The polygon-cutting theorem, which provides us with a balancing scheme, and
2. The planar separator theorem, whose role is essential in the discovery of new diagonals.

[Chazelle](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjUuZyBn7WCAxWFxgIHHWENB70QFnoECCIQAQ&url=https%3A%2F%2Fwww.cs.princeton.edu%2F~chazelle%2F&usg=AOvVaw21UQXRvLZSKJswAcOV4wW5&opi=89978449) and [Incerpi](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjd7b7uoLWCAxVA3gIHHetDCg0QFnoECBIQAQ&url=https%3A%2F%2Fwww-sop.inria.fr%2Fcroap%2Fpersonnel%2FJanet.Bertot%2FjmiCV.html&usg=AOvVaw2mb3Fc7XGWrZg_2k0i1Mq8&opi=89978449) showed how to build the visibility map of an n-vertex curve in **O(n log n)** time, using [divide and conquer](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjKiOekobWCAxVy0gIHHU4hAvsQFnoECBcQAQ&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FDivide-and-conquer_algorithm&usg=AOvVaw0hkGCEYFNx4omkeSLqAGY0&opi=89978449).
This algorithm mimics [mergesort](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiZ_deLobWCAxURMuwKHVGgDLAQFnoECBAQAQ&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMerge_sort&usg=AOvVaw2nk3iXDJE3NQYvPZ2sr_Ny&opi=89978449):
Assuming that n is a power of 2, at the *k*th stage(k=1,2,3,...,log n), the boundary of the polygon is decomposed into chains of size 2^k, whose visibility maps are computed by piecing together the maps obtained at the previous stage.
Each stage can be accomplished in a linear number of operations, so computing the visibility map of the polygon takes **O(n log n)** time.

The new algorithm follows the same pattern: It goes through an *up-phase* of log n stages, each involving the merging of maps obtained at the previous stage.

The novelty we bring into this process is to use only coarse samples of the visibility maps during the merges.

In this way we can carry out an entire stage in sub-linear time and death the *n log n* barrier.

The samples are uniform sub-maps of the visibility maps; uniform in the sense that they approximate the viability maps anywhere equally well.

Of course, in the end, we also need an efficient way to *refine* the sub-map derived for the whole polygon into its full-fledged visibility map.

After this is done, it takes only linear time to compute a triangulation.

To refine a sub-map we go down through stages in reverse (a down-phase):

Each transition refines the sub-map incrementally, until we get back to the first stage, at which point the full visibility map emerges at last.

Illustration of the up and down phase:
![[illustration.png]]
The polygon-cutting theorem is a geometric analog of the centroid theorem for free trees: a visibility map has a tree structure and, so, can be written as a collection of "blobs" of roughly equal size, themselves interconnected in a tree pattern.

These blobs are the constituents of a sub-map.

Merging two sub-maps can thus be equated with "merging" two trees together.

The [mergesort](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiZ_deLobWCAxURMuwKHVGgDLAQFnoECBAQAQ&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMerge_sort&usg=AOvVaw2nk3iXDJE3NQYvPZ2sr_Ny&opi=89978449) equivalent of a sub-map would be sub-list obtained by picking keys at regular intervals.

Notice that merging two such sublists might in the worst case produce a new sub0list whose corresponding intervals are up to twice the sizeof the original intervals.

This coarsening effect prevents us from speeding up [mergesort](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiZ_deLobWCAxURMuwKHVGgDLAQFnoECBAQAQ&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMerge_sort&usg=AOvVaw2nk3iXDJE3NQYvPZ2sr_Ny&opi=89978449), because repairing the damage might involve computing medians or things of that nature for which no shortcuts can be found.

To be sure, as we shall see, equally bad things can happen with sub-maps; repairing the damage, however, can be done by simply adding new chords to sub-maps, which can be made to take only sub-linear time.

To make this possible we must keep the coarseness of sub-maps under control by requiring that the tree structure of a sub-map be of bounded degree: in our terminology "conformal" actually means degree at means degree at most 4.

Restoring conformality after merging two sub-maps is is the linchpin of the algorithm and, as we should expect, its most delicate and subtle part as well: it can be viewed as a geometric "two-dimensional" analog of rotations in balanced dynamic search trees.

# Links
---
[Chazelle's main article](https://www.cs.princeton.edu/~chazelle/pubs/polygon-triang.pdf)
[Polygon-cutting theorem](https://www.cs.princeton.edu/techreports/1990/264.pdf)