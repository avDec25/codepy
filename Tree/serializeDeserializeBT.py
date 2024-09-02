# https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def preOrder(node):
    print(node.val, end=", ")

    if node.left is not None:
        preOrder(node.left)

    if node.right is not None:
        preOrder(node.right)


def postOrder(node):
    if node.left is not None:
        postOrder(node.left)

    if node.right is not None:
        postOrder(node.right)

    print(node.val, end=", ")


def inOrder(node):
    if node.left is not None:
        inOrder(node.left)

    print(node.val, end=", ")

    if node.right is not None:
        inOrder(node.right)


if __name__ == '__main__':
    root = Node(20)

    root.left = Node(8)
    root.right = Node(22)

    root.left.left = Node(4)
    root.left.right = Node(12)

    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    print("pre order : ")
    preOrder(root)

    print("\n\npost order: ")
    postOrder(root)

    print("\n\nin order  : ")
    inOrder(root)
