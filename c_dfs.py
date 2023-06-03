# a_bfs.py
## author - nick s.


import a_bst as BST
from a_bst import Node, Tree

# step 0 initialize a BST
tree: Tree = BST.initialize()

# step 1 insert items into BST
tree.root = BST.insert(tree.root, 0)
tree.root = BST.insert(tree.root, 1)
tree.root = BST.insert(tree.root, -2)
tree.root = BST.insert(tree.root, 10)
tree.root = BST.insert(tree.root, -10)
tree.root = BST.insert(tree.root, 5)
tree.root = BST.insert(tree.root, -5)

# verify tree
BST.preorder_traversal(tree.root)

# step 2 setup search space
start: Node = tree.root
search_space: list = [start]

# step 3 while the search space is empty...
while len(search_space) > 0:
    # remove a node from the search space (FIFO)
    current: Node = search_space.pop( None ) # TODO

    # if a None child is not being processed...
    if current != None:
        # print the node's value
        print(current.value)

        # add the left and right to the search space (FILO)
        search_space = None # TODO
    # end if
# end loop