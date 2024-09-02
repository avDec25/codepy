class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inOrder(root):
    global counter
    global k

    if root.left:
        inOrder(root.left)

    print(f"counter = {counter}")
    counter += 1
    if counter == k:
        print(root.val)
        return

    if root.right:
        inOrder(root.right)


if __name__ == '__main__':
    root = Node(20)

    root.left = Node(8)
    root.right = Node(22)

    root.left.left = Node(4)
    root.left.right = Node(12)

    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    k = 3
    counter = 0
    inOrder(root)
