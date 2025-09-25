# Binary tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value) # 0
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def go_through_in_order(self):
        self._go_through_in_recursive_order(self.root)

    def _go_through_in_recursive_order(self, current_node):
        if current_node is not None:
            self._go_through_in_recursive_order(current_node.left)
            print(current_node.value, end=" ")
            self._go_through_in_recursive_order(current_node.right)

tree = BinaryTree()
array = [0,1,10,29,11,0,32,34,56,22,90,21]

for i in array:
    tree.insert(i)

print("\nRESULT IN ORDER:")
tree.go_through_in_order()
print("\n")
