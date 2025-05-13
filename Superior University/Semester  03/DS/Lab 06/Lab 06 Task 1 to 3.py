# Task 1: Implementing a Binary Search Tree (BST) with Basic Operations

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right
    def search(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if not node:
            return None
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if not node.left and not node.right:
                return None
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            min_larger_node = self._find_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete_recursive(node.right, min_larger_node.value)
        return node

    def inorder_traversal(self):
        values = []
        self._inorder_recursive(self.root, values)
        print(" ".join(map(str, values)))

    def _inorder_recursive(self, node, values):
        if node:
            self._inorder_recursive(node.left, values)
            values.append(node.value)
            self._inorder_recursive(node.right, values)
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)
bst.inorder_traversal()  
#Task 02 : Finding the Lowest Common Ancestor (LCA) in a BST


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right
    def find_lca(self, node, value1, value2):
        if not node:
            return None
        if value1 < node.value and value2 < node.value:
            return self.find_lca(node.left, value1, value2)
        if value1 > node.value and value2 > node.value:
            return self.find_lca(node.right, value1, value2)
        return node  
    def get_lca(self, value1, value2):
        lca_node = self.find_lca(self.root, value1, value2)
        return lca_node.value if lca_node else None
bst = BinarySearchTree()
values = [20, 10, 30, 5, 15, 25, 35]
for v in values:
    bst.insert(v)

print(bst.get_lca(5, 15))  
print(bst.get_lca(5, 25))  
print(bst.get_lca(25, 35)) 

# Task :03 Checking if a Binary Tree is Balanced




class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_balanced(root):
    def check_height(node):
        if not node:
            return 0  
        left_height = check_height(node.left)
        right_height = check_height(node.right)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1
    return check_height(root) != -1  

root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(3)
root.left.right = Node(7)

print(is_balanced(root))  
root.right.right = Node(30)
root.right.right.right = Node(40)

print(is_balanced(root)) 