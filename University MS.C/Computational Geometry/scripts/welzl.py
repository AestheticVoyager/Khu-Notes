import random
import math

def welzl(points):
    if len(points) == 0:
        # return circle with infinite radius
        return (None, float('inf'))
    elif len(points) == 1:
        # return a circle centered at the only point with radius zero
        return (points[0], 0)

    # randomly select a point
    p = random.choice(points)

    # recursively compute the minimum enclosing circle for the remaining points
    circle = welzl([q for q in points if q != p])

    # if p lies inside the computed circle, return it
    if math.dist(circle[0], p) <= circle[1]:
        return circle
    # compute the minimum enclosing circle for the remaining points and p
    circle_prime = welzl([q for q in points if q != p] + [p])
    return circle_prime

if __name__ == '__main__':
    points = [(0, 0), (1, 0), (0, 1), (1, 1)]
    circle = welzl(points)
    center, radius = circle
    print("Center:", center)
    print("Radius:", radius)
