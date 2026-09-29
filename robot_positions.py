class PositionNode:
    def __init__(self, material_id, x, y, z):
        self.material_id = material_id  # The key we search for (Decimal value)
        self.coordinates = [x, y, z]  # Target X, Y, Z coordinate values
        self.left = None  # Left child node pointers
        self.right = None  # Right child node pointers


def insert_node(root, node):
    """Inserts a positional coordinate node into the BST."""
    if root is None:
        return node

    if node.material_id < root.material_id:
        root.left = insert_node(root.left, node)
    else:
        root.right = insert_node(root.right, node)
    return root


def search_bst(root, key):
    """
    Traverses the tree to find the target position coordinates.
    Execution speed scales at O(log n) time.
    """
    # Base Cases: root is null or key is present at root
    if root is None or root.material_id == key:
        return root

    # Key is smaller than root's key
    if key < root.material_id:
        return search_bst(root.left, key)

    # Key is greater than root's key
    return search_bst(root.right, key)


def initialize_coordinate_tree():

    # Root Node (A balanced middle ID like 8 prevents worst-case skewing)
    root = PositionNode(material_id=8, x=440, y=200, z=835)

    insert_node(root, PositionNode(material_id=1, x=860, y=200, z=835))
    insert_node(root, PositionNode(material_id=2, x=730, y=200, z=835))
    insert_node(root, PositionNode(material_id=3, x=680, y=200, z=835))
    insert_node(root, PositionNode(material_id=4, x=620, y=200, z=835))
    insert_node(root, PositionNode(material_id=6, x=670, y=200, z=835))

    insert_node(root, PositionNode(material_id=12, x=400, y=200, z=50)) # this line will never happen, just for better balance
    insert_node(root, PositionNode(material_id=16, x=330, y=200, z=835))
    insert_node(root, PositionNode(material_id=24, x=370, y=200, z=835))
    insert_node(root, PositionNode(material_id=32, x=200, y=200, z=835))
    insert_node(root, PositionNode(material_id=48, x=270, y=200, z=835))
    return root
