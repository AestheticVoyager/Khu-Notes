# Incremental Convex Builder
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def quicksort(arr, attr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = getattr(arr[0], attr)
        lesser = [x for x in arr[1:] if getattr(x, attr) <= pivot]
        greater = [x for x in arr[1:] if getattr(x, attr) > pivot]
        return quicksort(lesser, attr) + [arr[0]] + quicksort(greater, attr)

def right_turn(p1, p2, p3):
    cross_product = (p2.x - p1.x) * (p3.y - p2.y) - (p2.y - p1.y) * (p3.x - p2.x)
    return cross_product < 0  # Right turn if cross product is negative

def incremental_convex_hull(points):
    # Sorting points from left to right
    p = quicksort(points, 'x')
    n = len(p)
    l_upper = [p[0], p[1]]
    l_lower = [p[n - 1], p[n - 2]]

    # upper hull convex
    for j in range(2, n):
        l_upper.append(p[j])
        size = len(l_upper)
        while size > 2 and not right_turn(l_upper[size - 3], l_upper[size - 2], l_upper[size - 1]):
            l_upper.pop(size - 2)
            size = len(l_upper)

    # lower hull convex
    for j in reversed(range(0, n - 2)):
        l_lower.append(p[j])
        size = len(l_lower)
        while size > 2 and not right_turn(l_lower[size - 3], l_lower[size - 2], l_lower[size - 1]):
            l_lower.pop(size - 2)
            size = len(l_lower)
    l_lower.pop(0)
    l_lower.pop(len(l_lower) - 1)
    return l_lower + l_upper

def plot_polygon(all_points, convex_hull):
    x = [vertex.x for vertex in convex_hull]
    y = [vertex.y for vertex in convex_hull]

    # Add the first vertex at the end to close the polygon
    x += (x[0],)
    y += (y[0],)

    px = [point.x for point in all_points]
    py = [point.y for point in all_points]

    # Plotting
    plt.figure()
    plt.plot(x, y, label='Convex hull')  # polygon plotting
    plt.fill(x, y, alpha=0.3)
    plt.scatter(px, py, color='red', label='Points')
    plt.axis('equal')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Convex hull')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    points = [
        Point(3, 4),
        Point(4, 5),
        Point(6, 8),
        Point(6, 2),
        Point(4, -3),
        Point(2, -1),
        Point(2, -4),
        Point(0, -5),
        Point(-1, -1),
        Point(-9, -6),
        Point(-2, 1),
        Point(-1, 2),
    ]

    convex_hull = incremental_convex_hull(points)
    print("Convex hull:")
    for p in convex_hull:
        print(f'({p.x},{p.y})')
    plot_polygon(points, convex_hull)
