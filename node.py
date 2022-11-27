class Node:

  def __init__(self, value, right=None, left=None):
    self.value = value
    self.right = right
    self.left = left
    self.level = 0

  def __str__(self):
    return str(self.value)
