from binary_tree import BinaryTree

tree = BinaryTree()

tree.append(7)
tree.append(5)
tree.append(10)
tree.append(3)
tree.append(6)
tree.append(8)
tree.append(11)
#tree.show()

print(tree.search(7).left)
print(tree.search(7).right)
print(tree.search(7).level)
print()

print(tree.search(5).left)
print(tree.search(5).right)
print(tree.search(5).level)
print()

print(tree.search(3).level)
print(tree.search(11).level)
print()

#tree.show()

#print()
#print()
#print()

#print(tree.search(8).right)
#print(tree.search(7).right)
#print(tree.search(6).left)
#print(tree.search(6).right)
#print()
#tree.show()

#tree.remove(10)
#print(tree.search(7).left)
#print(tree.search(8).left)
#tree.remove(5)
#print(tree.search(7).left)
#print(tree.search(7).right)
