import networkx as nx
from sortedcontainers import SortedList

class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class HalfEdge:
    def __init__(self):
        self.origin = None
        self.twin = None
        self.next = None
        self.prev = None
        self.incident_face = None

class FaceRecord:
    def __init__(self):
        self.outer_component = None
        self.inner_components = []

class Face:
    def __init__(self, name=None):
        self.outer_component = None
        self.inner_components = []  # List to store inner components
        self.name = name

class DoublyConnectedEdgeList:
    def __init__(self):
        self.vertices = []
        self.half_edges = []
        self.faces = []

class Event:
    def __init__(self, x, edge, event_type):
        self.x = x
        self.edge = edge
        self.event_type = event_type  # "Left" or "Right"

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        if node is not None:
            node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, root, key):
        if root is None:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        self.update_height(root)

        balance = self.balance_factor(root)

        # Left Heavy
        if balance > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        # Right Heavy
        if balance < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

def copy_doubly_connected_edge_lists(S):
    D = DoublyConnectedEdgeList()

    # Copy vertices
    for vertex in S.vertices:
        D.vertices.append(Vertex(vertex.x, vertex.y))

    # Copy half edges
    for edge in S.half_edges:
        new_edge = HalfEdge()
        new_edge.origin = D.vertices[edge.origin.index]
        new_edge.twin = None
        new_edge.next = None
        new_edge.prev = None
        new_edge.incident_face = None
        D.half_edges.append(new_edge)

    # Copy faces
    for face in S.faces:
        new_face = Face()
        new_face.outer_component = None
        D.faces.append(new_face)

    # Set twin, next, prev, and incident_face for the new half edges
    for i, edge in enumerate(S.half_edges):
        D.half_edges[i].twin = D.half_edges[edge.twin.index] if edge.twin else None
        D.half_edges[i].next = D.half_edges[edge.next.index] if edge.next else None
        D.half_edges[i].prev = D.half_edges[edge.prev.index] if edge.prev else None
        D.half_edges[i].incident_face = D.faces[edge.incident_face.index] if edge.incident_face else None

    # Set outer_component for the new faces
    for i, face in enumerate(S.faces):
        D.faces[i].outer_component = D.half_edges[face.outer_component.index] if face.outer_component else None

    return D

def compute_intersections(S1, S2):
    D = copy_doubly_connected_edge_lists(S1)  # Copy S1 to D
    events = SortedList()

    # Add events for edges in S1
    for edge in S1.half_edges:
        events.add(Event(edge.origin.x, edge, "Left"))
        events.add(Event(edge.next.origin.x, edge, "Right"))

    # Add events for edges in S2
    for edge in S2.half_edges:
        events.add(Event(edge.origin.x, edge, "Left"))
        events.add(Event(edge.next.origin.x, edge, "Right"))

    T = AVLTree()  # AVL tree for handling intersections

    while events:
        event = events.pop(0)

        if event.event_type == "Left":
            handle_left_event(event, T, D)
        elif event.event_type == "Right":
            handle_right_event(event, T, D)

    return D

def handle_left_event(event, T, D):
    T.insert_key(event.x)

    left_edge = D.half_edges[D.half_edges.index(event.edge) - 1]
    intersection_point = find_intersection(left_edge, event.edge)
    
    if intersection_point:
        update_D(D, event.edge, left_edge, intersection_point)

def handle_right_event(event, T, D):
    T.delete_key(event.x)


def find_intersection(edge1, edge2):
    # Extract coordinates of the endpoints of the first edge
    x1, y1 = edge1.origin.x, edge1.origin.y
    x2, y2 = edge1.twin.origin.x, edge1.twin.origin.y

    # Extract coordinates of the endpoints of the second edge
    x3, y3 = edge2.origin.x, edge2.origin.y
    x4, y4 = edge2.twin.origin.x, edge2.twin.origin.y

    # Check if the edges are parallel using determinant
    det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if det == 0:
        return None  # Edges are parallel, no intersection

    # Calculate parameters for the intersection point
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / det
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / det

    # Check if the intersection point is within the parameter range [0, 1] for both edges
    if 0 <= t <= 1 and 0 <= u <= 1:
        # Calculate the coordinates of the intersection point
        intersection_x = x1 + t * (x2 - x1)
        intersection_y = y1 + t * (y2 - y1)

        return Vertex(intersection_x, intersection_y)
    else:
        return None  # Intersection point is outside the parameter range

def update_D(D, edge1, edge2, intersection_point):
    # Update D as explained in the algorithm
    new_edge1 = HalfEdge()
    new_edge2 = HalfEdge()

    # Set origins and twins
    new_edge1.origin = intersection_point
    new_edge1.twin = new_edge2
    new_edge2.origin = intersection_point
    new_edge2.twin = new_edge1

    # Set next and prev pointers
    new_edge1.next = edge1
    new_edge1.prev = edge2.prev
    new_edge2.next = edge2
    new_edge2.prev = edge1.prev

    # Update next and prev pointers of adjacent edges
    edge1.prev.next = new_edge1
    edge1.prev = new_edge2
    edge2.prev.next = new_edge2
    edge2.prev = new_edge1

    # Update incident_face pointers
    new_edge1.incident_face = edge1.incident_face
    new_edge2.incident_face = edge2.incident_face

    # Update the doubly-connected edge list
    D.half_edges.extend([new_edge1, new_edge2])

def compute_faces(D):
    unvisited_edges = set(D.half_edges)
    unvisited_faces = set(D.faces)

    while unvisited_edges:
        edge = unvisited_edges.pop()

        if edge in unvisited_edges:
            continue

        start_edge = edge
        current_face = Face()

        while True:
            unvisited_edges.discard(edge)
            unvisited_faces.discard(current_face)

            if edge.incident_face is None:
                edge.incident_face = current_face
                current_face.outer_component = edge

            twin = edge.twin

            if twin in unvisited_edges:
                edge = twin
            else:
                edge = twin.next

            if edge == start_edge:
                break

        D.faces.append(current_face)

    return D

def determine_boundary_cycles(D):
    boundary_cycles = []

    for face in D.faces:
        if face.outer_component is not None:
            cycle = traverse_cycle(face.outer_component)
            if cycle:
                boundary_cycles.append(cycle)

    return boundary_cycles

def traverse_cycle(start_edge):
    cycle = []
    current_edge = start_edge

    while current_edge not in cycle:
        cycle.append(current_edge)
        current_edge = current_edge.next

    return cycle if len(cycle) > 2 else None

def construct_graph_and_connected_components(boundary_cycles):
    G = nx.DiGraph()

    # Add nodes for boundary cycles
    for i, cycle in enumerate(boundary_cycles):
        G.add_node(i, cycle=cycle)

    # Connect hole cycles to the cycle to the left of their leftmost vertex
    for i, cycle in enumerate(boundary_cycles):
        leftmost_vertex = find_leftmost_vertex(cycle)
        for j, other_cycle in enumerate(boundary_cycles):
            if i != j and is_vertex_inside_cycle(leftmost_vertex, other_cycle):
                G.add_edge(j, i)

    # Compute connected components
    connected_components = list(nx.strongly_connected_components(G))

    return G, connected_components

def find_leftmost_vertex(cycle):
    leftmost_vertex = cycle[0].origin
    for edge in cycle:
        if edge.origin.x < leftmost_vertex.x:
            leftmost_vertex = edge.origin
    return leftmost_vertex

def is_vertex_inside_cycle(vertex, cycle):
    # Check if the vertex is inside the cycle using the ray-casting algorithm
    x, y = vertex.x, vertex.y
    is_inside = False

    for edge in cycle:
        x1, y1 = edge.origin.x, edge.origin.y
        x2, y2 = edge.twin.origin.x, edge.twin.origin.y

        # Check if the vertex is on the edge
        if ((y1 <= y < y2) or (y2 <= y < y1)) and (x < max(x1, x2)):
            if x1 != x2:
                x_intersect = (y - y1) * (x2 - x1) / (y2 - y1) + x1

            # Count intersections to the right of the vertex
            if x_intersect > x:
                is_inside = not is_inside

    return is_inside


def process_connected_components(G, connected_components, boundary_cycles, D):
    face_records = []

    for component in connected_components:
        outer_cycle_index = component.pop()
        outer_cycle = boundary_cycles[outer_cycle_index]
        outer_component = outer_cycle[0]

        face_record = FaceRecord(outer_component)
        face_records.append(face_record)

        for inner_cycle_index in component:
            inner_cycle = boundary_cycles[inner_cycle_index]
            inner_component = inner_cycle[0]
            face_record.inner_components.append(inner_component)

            for edge in inner_cycle:
                edge.incident_face = face_record

    return face_records

def label_faces_with_names(D, S1, S2):
    for face_record in D.faces:
        outer_component = face_record.outer_component

        face_in_S1 = find_containing_face(outer_component, S1)
        if face_in_S1:
            face_record.name_in_S1 = face_in_S1.name

        face_in_S2 = find_containing_face(outer_component, S2)
        if face_in_S2:
            face_record.name_in_S2 = face_in_S2.name

        for inner_component in face_record.inner_components:
            inner_face_in_S1 = find_containing_face(inner_component, S1)
            if inner_face_in_S1:
                face_record.inner_names_in_S1.append(inner_face_in_S1.name)

            inner_face_in_S2 = find_containing_face(inner_component, S2)
            if inner_face_in_S2:
                face_record.inner_names_in_S2.append(inner_face_in_S2.name)
    
    for connected_component in connected_components:
        for face in connected_component:
            face_record = FaceRecord()
            face_record.outer_component = face

            current_edge = face_record.outer_component.next
            while current_edge != face_record.outer_component:
                face_record.inner_components.append(current_edge)
                current_edge = current_edge.next

def find_containing_face(half_edge, subdivision):
    for face in subdivision.faces:
        if is_half_edge_inside_face(half_edge, face):
            return face
    return None

def is_half_edge_inside_face(half_edge, face):
    current_edge = face.outer_component
    while True:
        if current_edge == half_edge:
            return True
        current_edge = current_edge.next
        if current_edge == face.outer_component:
            break

    for inner_component in face.inner_components:
        current_edge = inner_component
        while True:
            if current_edge == half_edge:
                return True
            current_edge = current_edge.next
            if current_edge == inner_component:
                break
    return False

if __name__ == "__main__":
    # Assuming you have instances of S1 and S2
    S1 = DoublyConnectedEdgeList()  # Replace with your actual instance
    S2 = DoublyConnectedEdgeList()  # Replace with your actual instance

    # Example instances of S1 and S2
    S1 = DoublyConnectedEdgeList()
    S2 = DoublyConnectedEdgeList()

    # Define vertices for S1
    v1 = Vertex(0, 0)
    v2 = Vertex(1, 0)
    v3 = Vertex(1, 1)
    v4 = Vertex(0, 1)

    # Define edges for S1
    e1 = HalfEdge()
    e1.origin = v1
    e1.twin = None  # Update the twin later
    e1.next = None  # Update the next later
    e1.prev = None  # Update the prev later
    e1.incident_face = None  # Update the incident_face later

    e2 = HalfEdge()
    e2.origin = v2
    e2.twin = None
    e2.next = None
    e2.prev = None
    e2.incident_face = None

    e3 = HalfEdge()
    e3.origin = v3
    e3.twin = None
    e3.next = None
    e3.prev = None
    e3.incident_face = None

    e4 = HalfEdge()
    e4.origin = v4
    e4.twin = None
    e4.next = None
    e4.prev = None
    e4.incident_face = None

    # Update twins, next, prev, and incident_face pointers for S1
    e1.twin = e3
    e1.next = e2
    e1.prev = e4
    e2.twin = None  # Update the twin later
    e2.next = e3
    e2.prev = e1
    e3.twin = e1
    e3.next = e4
    e3.prev = e2
    e4.twin = e2
    e4.next = e1
    e4.prev = e3

    # Update incident_face pointers for S1
    e1.incident_face = None  # Update the incident_face later
    e2.incident_face = None
    e3.incident_face = None
    e4.incident_face = None

    # Define vertices for S2
    v5 = Vertex(0.5, 0.5)
    v6 = Vertex(1.5, 0.5)
    v7 = Vertex(1.5, 1.5)
    v8 = Vertex(0.5, 1.5)

    # Define edges for S2
    e5 = HalfEdge()
    e5.origin = v5
    e5.twin = None  # Update the twin later
    e5.next = None  # Update the next later
    e5.prev = None  # Update the prev later
    e5.incident_face = None  # Update the incident_face later

    e6 = HalfEdge()
    e6.origin = v6
    e6.twin = None
    e6.next = None
    e6.prev = None
    e6.incident_face = None

    e7 = HalfEdge()
    e7.origin = v7
    e7.twin = None
    e7.next = None
    e7.prev = None
    e7.incident_face = None

    e8 = HalfEdge()
    e8.origin = v8
    e8.twin = None
    e8.next = None
    e8.prev = None
    e8.incident_face = None

    # Update twins, next, prev, and incident_face pointers for S2
    e5.twin = e7
    e5.next = e6
    e5.prev = e8
    e6.twin = None  # Update the twin later
    e6.next = e7
    e6.prev = e5
    e7.twin = e5
    e7.next = e8
    e7.prev = e6
    e8.twin = e6
    e8.next = e5
    e8.prev = e7

    # Update incident_face pointers for S2
    e5.incident_face = None  # Update the incident_face later
    e6.incident_face = None
    e7.incident_face = None
    e8.incident_face = None

    # Update incident_face pointers for S1 and S2
    e1.incident_face = Face(name="S1_Face1")  # Create Face instances for S1 and S2
    e2.incident_face = e1.incident_face
    e3.incident_face = e1.incident_face
    e4.incident_face = e1.incident_face

    e5.incident_face = Face(name="S2_Face2")
    e6.incident_face = e5.incident_face
    e7.incident_face = e5.incident_face
    e8.incident_face = e5.incident_face


    # Update the faces for S1 and S2
    S1.faces = [e1.incident_face]
    S2.faces = [e5.incident_face]

    # Run the overlay algorithm
    D = compute_intersections(S1, S2)
    D = compute_faces(D)
    boundary_cycles = determine_boundary_cycles(D)
    G, connected_components = construct_graph_and_connected_components(boundary_cycles)
    face_records = process_connected_components(G, connected_components, boundary_cycles, D)
    label_faces_with_names(D, S1, S2)
