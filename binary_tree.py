from node import Node

ROOT = 'root'


class BinaryTree:

  def __init__(self):
    self.root = None

  def travel(self, node=None):
    if node is None:
      node = self.root
    if node.left:
      print('(', end='')
      self.travel(node.left)
    print(node, end='')

    if node.right:
      self.travel(node.right)
      print(')', end='')
#----------------------------------------------------------------------------------

  def append(self, value):  #adiciona um nó
    node = Node(value)

    if self.root is None:  #se a raiz for vazia,
      self.root = node
    else:
      self.add(value, self.root)

  def add(self, value, node):
    if value < node.value:
      if node.left is not None:  #se o valor for menor que a raiz, ele é adicionado à esquerda
        self.add(value, node.left)
      else:
        node.left = Node(value)

    else:
      if node.right is not None:  #se o valor for maior que a raiz, ele é adicionado à direita
        self.add(value, node.right)
      else:
        node.right = Node(value)
#----------------------------------------------------------------------------------

  def min(self, node=ROOT):
    if node == self.root:
      node = self.root
    while node.left:
      node = node.left
    return node.value

  def remove(self, value, node=ROOT):  #remove um nó
    if node == ROOT:
      node = self.root
    if node is None:
      return node

    if value < node.value:
      node.left = self.remove(value, node.left)
    elif value > node.value:
      node.right = self.remove(value, node.right)
    else:
      if node.left is None:
        return node.right
      elif node.right is None:
        return node.left
      else:
        aux = self.min(node.right)
        node.value = aux
        node.right = self.remove(aux, node.right)
    return node

#--------------------------------------------------------------------------------

  def show(self):  #mostra a árvore
    if self.root is not None:
      self.printTree(self.root)

  def printTree(self, node):

    if node is None:
      node = self.root
    if node.left:
      print('(', end='')
      self.printTree(node.left)
    #print('\n')
    print(node.value, end='')

    if node.right:
      self.printTree(node.right)

    print(')', end='')

  # if node is not None:
  #  print(str(node.value), end='\n')
  # self.printTree(node.left, )
  #self.printTree(node.right)


#-------------------------------------------------------------------------------

  def search(self, value):  #percorre a árvore e acha um valor
    if self.root is not None:
      return self.find(value, self.root)
    else:
      return None

  def find(self, value, node):  #acha um valor
    if value == node.value:
      return node
    elif (value < node.value and node.left is not None):
      return self.find(value, node.left)
    elif (value > node.value and node.right is not None):
      return self.find(value, node.right)
