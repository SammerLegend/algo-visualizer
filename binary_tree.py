class BinaryTree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = self.Node(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = self.Node(value)
                    return
                current = current.right

    def inorder(self):
        result = []

        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            result.append(node.value)
            traverse(node.right)

        traverse(self.root)
        return result
