from binary_tree import BinaryTree

tree = BinaryTree()

tree.append(7)
tree.append(5)
tree.append(10)
tree.append(3)
tree.append(6)
tree.append(8)

tree.show()

tree.deleteNode(5, 3)

tree.show()
