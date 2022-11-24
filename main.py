from binary_tree import BinaryTree

tree = BinaryTree()

tree.append(7)
tree.append(5)
tree.append(10)
tree.append(3)
tree.append(6)
tree.append(8)
tree.append(11)

print(tree.search(5).left)
print(tree.search(5).right)
tree.show()

print()
print()
print()

tree.remove(5)
print(tree.search(6).left)
print(tree.search(7).left)
tree.show()

tree.remove(10)
print(tree.search(8).left)
print(tree.search(7).right)
