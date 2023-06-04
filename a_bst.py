# a_bst.py
## author - Gregory L.


class Node:
    value: any
    left: any
    right: any

    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.value = val


class Tree:
    root: Node
    def __init__(self, root=None):
        self.root = root


def initialize() -> Tree:
    return Tree(None)


def isEmpty(tree: Tree) -> bool:
    if tree.root is None:
        return True
    return False


def height(root: Node) -> int:
    if root is None:
        return 0
    else:
        h_left: int = height(root.left)
        h_right: int = height(root.right)
        return max(h_left, h_right) + 1


def preorder_traversal(tree: Node, level:int=0):
    if level == 0:
        print('pre order traversal')
    if tree != None:
        print(f' level = {level:^3d} : value = {tree.value}')
        preorder_traversal(tree.left, level+1)
        preorder_traversal(tree.right, level+1)


def inorder_traversal(tree: Node, level:int=0):
    if level == 0:
        print('in order traversal')
    if tree != None:
        inorder_traversal(tree.left, level+1)
        print(f' level = {level:^3d} : value = {tree.value}')
        inorder_traversal(tree.right, level+1)


def postorder_traversal(tree: Node, level:int=0):
    if level == 0:
        print('post order traversal')
    if tree != None:
        postorder_traversal(tree.left, level+1)
        postorder_traversal(tree.right, level+1)
        print(f' level = {level:^3d} : value = {tree.value}')


def search(root: Node, value: int) -> Node:
    # base cases
    if root.value == value:
        return root #Found it!
    if value < root.value and root.left is not None: #If smaller, go left
        return search(root.left, value)
    elif value > root.value and root.right is not None: #If bigger, go right
        return search(root.right, value)
    else:
        return None #Didn't find the value


# NOT given to students
def insert(root: Node, value: int) -> Node:
    if root is None: #If empty tree
        root = Node(value, None, None)
    elif value < root.value and root.left is None: #If value is smaller and left slot is empty, make new node
        root.left = Node(value, None, None)
    elif value < root.value and root.left is not None: #If value is smaller and left slot not empty, try to insert farther down the tree
        root.left = insert(root.left, value)
    elif value > root.value and root.right is None:
        root.right = Node(value, None, None)
    else:
        root.right = insert(root.right, value)
    return root


def remove(root: Node, value: int) -> Node:
    def getMin(v: Node):
        current = v
        while current.left is not None:
            current = current.left
        return current
    if root is None:
        return None
    if value < root.value:
        root.left = remove(root.left, value)
    elif value > root.value:
        root.right = remove(root.right, value)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = getMin(root.right)
        root.value = temp.value
        root.right = remove(root.right, temp.value)
    return root


# given to students
# uses in order traversal
def storeNodes(v: Node, nodes:list):
    if v is None:
        return
    else:
        storeNodes(v.left, nodes)
        nodes.append(v)
        storeNodes(v.right, nodes)


num_iter: int = 0

# given to students
def balance_tree(tree: Tree) -> Tree:
    global num_iter
    def helper(nodes: list, start: int, end: int) -> Node:
        global num_iter
        num_iter += 1
        if start > end:
            return None
        else:
            mid: int = (start + end) // 2 # you divide by two
            w: Node = nodes[mid]
            w.left = helper(nodes, start, mid - 1) # you do half work (first time)
            w.right = helper(nodes, mid + 1, end) # you do half work (second time)
            return w
    # end helper
    nodes: list = list()
    storeNodes(tree.root, nodes)
    n: int = len(nodes)
    tree.root = helper(nodes, 0, n - 1)
    print(f'num iters to balance {num_iter}')
    return tree
