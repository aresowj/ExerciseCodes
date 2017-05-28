import six
import copy

"""Quad Tree Implementation in Python

Requirements
● Each node
    ○ has a bounding box that’s rectangular in shape
    ○ can store a coordinate
● Coordinates that can be inserted into a particular node should fall within the node’s
bounding box.
● If the point falls within the bounding box of the current node but a point is already stored
at the node, we need to figure out which child node we should try to store the point at.
The appropriate child node should be determined by the quadrant the point falls within
the current node’s bounding box(see pic 1). A coordinate of (1, 5) would fall within the
southwest quadrant of the bounding box.
"""


NORTH_WEST = 'north_west'
NORTH_EAST = 'north_east'
SOUTH_WEST = 'south_west'
SOUTH_EAST = 'south_east'
CHILDREN_NAMES = (NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST)


class Coordinate(object):
    """Coordinate class to store the x an y position of a point"""

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def _check_integer(val):
        if not isinstance(val, six.integer_types):
            raise ValueError('Coordination should be an integer!')

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        self._check_integer(val)
        self._x = val;
    
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        self._check_integer(val)
        self._y = val;


class Boundary(object):
    def __init__(self, center, half_width, half_height):
        self.x = center.x
        self.y = center.y
        self.half_height = half_height
        self.half_width = half_width
        # Calculate margins for future use
        self.left_margin = self.x - self.half_width
        self.right_margin = self.x + self.half_width
        self.top_margin = self.y + self.half_height
        self.bottom_margin = self.y - self.half_height

    def in_bound(self, coordinate):
        return self.left_margin <= coordinate.x <= self.right_margin \
                and self.bottom_margin <= coordinate.y <= self.top_margin


class Node(object):
    def __init__(self, boundary, parent=None):
        self._boundary = boundary
        self._parent = parent
        self._coordinates = {}

        # A node in a quad-tree should have exactly four children (via Wikipedia)
        self._children = {
            NORTH_WEST: None,
            NORTH_EAST: None,
            SOUTH_WEST: None,
            SOUTH_EAST: None,
        }

    def _check_coordinate(self, coordinate):
        if not self.in_bound(coordinate):
            raise ValueError('This coordinate is out of bound, cannot not be inserted!')
        if not isinstance(coordinate, Coordinate):
            raise ValueError('The coordinate should be an instance of Coordinate class!')

    def insert(self, coordinate):
        """Insert a coordinate in this node. We assume that multple points could
        be stored in a single node."""
        self._check_coordinate(coordinate)

        name = str(coordinate.x) + ', ' + str(coordinate.y)
        if name in self._coordinates:
            # If already stored, put the point in a child node.
            child_name = self.find_child(coordinate)
            if self._children[child_name] is None:
                self._make_children()
            self._children[child_name].insert(coordinate)
        else:
            # Make a copy to avoid the object being deleted in the future.
            self._coordinates[name] = copy.deepcopy(coordinate)

    def in_bound(self, coordinate):
        return self._boundary.in_bound(coordinate)

    def find_child(self, coordinate):
        if coordinate.x >= self._boundary.x and coordinate.y >= self._boundary.y:
            return NORTH_EAST
        elif coordinate.x >= self._boundary.x and coordinate.y < self._boundary.y:
            return SOUTH_EAST
        elif coordinate.x < self._boundary.x and coordinate.y >= self._boundary.y:
            return NORTH_WEST
        else:
            return SOUTH_WEST

    def _make_quadrant(self, child_name):
        half_height = self._boundary.half_height / 2.0
        half_width = self._boundary.half_width / 2.0

        if child_name == NORTH_WEST:
            center = Coordinate(self._boundary.x - half_width, self._boundary.y + half_height)
            return Boundary(center, half_width, half_height)
        elif child_name == NORTH_EAST:
            center = Coordinate(self._boundary.x + half_width, self._boundary.y + half_height)
            return Boundary(center, half_width, half_height)
        elif child_name == SOUTH_WEST:
            center = Coordinate(self._boundary.x - half_width, self._boundary.y - half_height)
            return Boundary(center, half_width, half_height)
        elif child_name == SOUTH_EAST:
            center = Coordinate(self._boundary.x + half_width, self._boundary.y - half_height)
            return Boundary(center, half_width, half_height)

    def _make_children(self):
        """Make the four children boundary lazily."""
        for name in CHILDREN_NAMES:
            self._children[name] = Node(self._make_quadrant(name), self)


if __name__ == '__main__':
    # Some tests
    # Make a square boundary
    boundary = Boundary(Coordinate(50, 10), 50, 10)
    # Root node
    quad_tree = Node(boundary)
    # Children should be made lazily
    for name, child in six.iteritems(quad_tree._children):
        assert child is None
        
    quad_tree.insert(Coordinate(1, 1))
    # See if the point is stored
    assert quad_tree._coordinates['1, 1'].x == 1
    assert quad_tree._coordinates['1, 1'].y == 1
    
    try:
        quad_tree.insert(Coordinate(100, 100))
    except ValueError:
        print('Out of bound test OK')

    # Insert the same point again, children should be made and store
    # the duplicate point. The point should be in the south west child.
    quad_tree.insert(Coordinate(1, 1))
    for name, child in six.iteritems(quad_tree._children):
        assert child is not None

    assert quad_tree._children[SOUTH_WEST]._coordinates['1, 1'].x == 1
    assert quad_tree._children[SOUTH_WEST]._coordinates['1, 1'].y == 1

    # Center point of south west child should be (25, 5)
    assert quad_tree._children[SOUTH_WEST]._boundary.x == 25
    assert quad_tree._children[SOUTH_WEST]._boundary.y == 5
