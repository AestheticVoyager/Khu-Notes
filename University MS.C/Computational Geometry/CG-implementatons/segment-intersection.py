import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from itertools import combinations


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Segment:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def upper_endpoint(self):
        return max(self.start, self.end, key=lambda p: p.y)

    def intersects(self, other):
        return self.segment_intersection(
            (self.start.x, self.start.y),
            (self.end.x, self.end.y),
            (other.start.x, other.start.y),
            (other.end.x, other.end.y)
        )

    @staticmethod
    def segment_intersection(p1, q1, p2, q2):
        def line_from_points(P, Q):
            A = Q[1] - P[1]
            B = P[0] - Q[0]
            C = A * P[0] + B * P[1]
            return A, B, -C

        def intersection(L1, L2):
            D = L1[0] * L2[1] - L1[1] * L2[0]
            Dx = L1[2] * L2[1] - L1[1] * L2[2]
            Dy = L1[0] * L2[2] - L1[2] * L2[0]
            return (-Dx / D, -Dy / D) if D != 0 else None

        def on_segment(p, q, r):
            return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
                    min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

        L1 = line_from_points(p1, q1)
        L2 = line_from_points(p2, q2)

        R = intersection(L1, L2)

        if R and all(on_segment(p1, R, q1) and on_segment(p2, R, q2) for p1, q1, p2, q2 in [(p1, q1, p2, q2), (p2, q2, p1, q1)]):
            return R
        else:
            return None


def find_intersections(segments):
    intersections = []

    for segment1, segment2 in combinations(segments, 2):
        intersection_point = segment1.intersects(segment2)
        if intersection_point:
            intersections.append((segment1, segment2, intersection_point))

    return intersections


def visualize_segments_intersections(segments, intersections):
    fig, ax = plt.subplots()

    for segment in segments:
        line = mlines.Line2D([segment.start.x, segment.end.x], [segment.start.y, segment.end.y], color='blue')
        ax.add_line(line)

    for intersection in intersections:
        ax.plot(intersection[2][0], intersection[2][1], 'ro')  # Red dot for intersections

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Segment Intersections Visualization')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    p1 = Point(x=2, y=3)
    q1 = Point(x=8, y=12)
    p2 = Point(x=2, y=6)
    q2 = Point(x=10, y=6)
    p3 = Point(x=6, y=9)
    q3 = Point(x=12, y=3)

    segments = [Segment(start=p1, end=q1), Segment(start=p2, end=q2), Segment(start=p3, end=q3)]
    result = find_intersections(segments)
    visualize_segments_intersections(segments, result)
