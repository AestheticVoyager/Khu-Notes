## Ear clipping method
One way to triangulate a simple polygon is based on the [two ears theorem](https://en.wikipedia.org/wiki/Two_ears_theorem "Two ears theorem"), as the fact that any simple polygon with at least 4 vertices without holes has at least two '[ears](https://en.wikipedia.org/wiki/Ear_(mathematics) "Ear (mathematics)")', which are triangles with two sides being the edges of the polygon and the third one completely inside it.
The algorithm then consists of finding such an ear, removing it from the polygon (which results in a new polygon that still meets the conditions) and repeating until there is only one triangle left.

This algorithm is easy to implement, but slower than some other algorithms, and it only works on polygons without holes. An implementation that keeps separate lists of convex and concave vertices will run in O(n^2) time. 
This method is known as _ear clipping_ and sometimes _ear trimming_. An efficient algorithm for cutting off ears was discovered by Hossam ElGindy, Hazel Everett, and [Godfried Toussaint](https://en.wikipedia.org/wiki/Godfried_Toussaint "Godfried Toussaint").

