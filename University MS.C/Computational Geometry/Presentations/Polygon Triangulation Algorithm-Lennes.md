## Ear clipping method
One way to triangulate a simple polygon is based on the [two ears theorem](https://en.wikipedia.org/wiki/Two_ears_theorem "Two ears theorem"), as the fact that any simple polygon with at least 4 vertices without holes has at least two '[ears](https://en.wikipedia.org/wiki/Ear_(mathematics) "Ear (mathematics)")', which are triangles with two sides being the edges of the polygon and the third one completely inside it.
The algorithm then consists of finding such an ear, removing it from the polygon (which results in a new polygon that still meets the conditions) and repeating until there is only one triangle left.

This algorithm is easy to implement, but slower than some other algorithms, and it only works on polygons without holes. An implementation that keeps separate lists of convex and concave vertices will run in O(n^2) time. 
This method is known as _ear clipping_ and sometimes _ear trimming_. An efficient algorithm for cutting off ears was discovered by Hossam ElGindy, Hazel Everett, and [Godfried Toussaint](https://en.wikipedia.org/wiki/Godfried_Toussaint "Godfried Toussaint").

## Pseudo Code Ear Cutting Method
```C
struct PolygonTree
{
	Polygon p;
	array<PolygonTree> children;
};

array<Triangle> triangles;
PolygonTree tree = <some tree of polygons>;
queue<PolygonTree> Q;
Q.insertRear(tree);
while (not Q.empty()) do
{
	PolygonTree outerNode = Q.removeFront();
	numChildren = outerNode.children.quantity();
	if (numChildren == 0)
	{
		// The outer polygon is a simple polygon with no nested inner polygons.
		triangles.append(GetEarClipTriangles(outerNode.p));
	}
	else
	{
		// The outer polygon contains inner polygons
		for (i = 0; i < numChildren; i++)
		{
			PolygonTree innerNode = outerNode.children[i];
			array<Polygon> innerPolygons;
			numGrandchildren = innerNode.children.quantity();
			for (j = 0; j < numGrandchildren; j++)
			{
				innerPolygons.append(innerNode.p);
				Q.insertFront(innerNode.children[j]);
			}
			Polygon combined = MakeSimple(outerNode.p, innerPolygons);
			triangles.append(GetEarClipTriangles(combined));
		}	
	}
}
```
[source for pseudocode](https://www.geometrictools.com/Documentation/TriangulationByEarClipping.pdf)
# Implementation in Python
```Python
from math import atan2

class Point:
	'''
	class to represent a point in 2D space:
	X: float
	Y: float
	'''
	def __init__(self, x: float, y: float):
		self.x = x
		self.y = y
class Triangle:
	def __init__(self, p1: Point, p2: Point, p3: Point):
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3
	def is_ear(self, point: Point):
		# Calculate the angles formed by the point and the triangle vertices
		angle1 = self._calculate_angle(self.p1, self.p2, point)
		angle2 = self._calculate_angle(self.p2, self.p3, point)
		angle3 = self._calculate_angle(self.p3, self.p1, point)
		# Check if the angles are less than 180 degrees(pi radians)
		return angle1 + angle2 + angle3 < 2 * atan2(1, 0)
	def _calculate_angle(self, p1: Point, p2: Point, p3:Point):
		'''
		Calculate the angle formed by the 3 points
		'''
		# Calculate the vectors between the points
		v1 = Point(p1.x - p2.x, p1.y - p2.y)
		v2 = Point(p3.x - p2.x, p3.y - p2.y)
		# Calculate the dot product and the magnitudes of the vectors	
		dot_product = v1.x * v2.x + v1.y * v2.y
		magnitude_v1 = (v1.x ** 2 + v1.y ** 2) ** 0.5
		magnitude_v2 = (v2.x ** 2 + v2.y ** 2) ** 0.5
		# Calculate the angle using the dot product and magnitudes	
		angle = atan2(dot_product, magnitude_v1 * magnitude_v2)
		return angle

def ear_clipping(points):
	'''
	Implements the ear clipping algorithm to triangulate a polygon in 2D
	Returns a list of triangles.
	'''
	triangles = []
	# Copy the points to avoid moddifying the original list
	polygon = points.copy()
	while len(polygon) >= 3:
		for i in range(len(polygon)):
			p1 = polygon[i]
			p2 = polygon[(i + 1) % len(polygon)]
			p3 = polygon[(i + 2) % len(polygon)]
			triangle = Triangle(p1, p2, p3)
			is_ear = True
			for point in polygon:
				if point != p1 and point != p2 and point != p3 and triangle.is_ear(point):
					is_ear = False
					break
			if is_ear:
				triangles.append(triangle)
				polygon.remove(p2)
				break
	return triangles

if __name__ == "__main__":
	points = [
		Point(0,0),
		Point(1,0),
		Point(1,1),
		Point(0.5,1.5),
		Point(0,1)
	]
	triangles = ear_clipping(points)

	for i, triangle in enumerate(triangles):
		print(f"Triangle {i + 1}:")
		print(f"  Vertex 1: ({triangle.p1.x}, {triangle.p1.y})")
		print(f"  Vertex 2: ({triangle.p2.x}, {triangle.p2.y})")
		print(f"  Vertex 3: ({triangle.p3.x}, {triangle.p3.y})")
		print()
```
## Links
----
[link to article](https://www.geometrictools.com/Documentation/TriangulationByEarClipping.pdf)
