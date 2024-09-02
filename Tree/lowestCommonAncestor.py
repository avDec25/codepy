class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return f"({self.val})"


def lca(root, n1, n2):
    if root is None: return None

    # first node which is in between n1 and n2
    if n1 <= root.val <= n2:
        return root

    if root.val > n2:
        return lca(root.left, n1, n2)
    if root.val < n1:
        return lca(root.right, n1, n2)


if __name__ == '__main__':
    root = Node(20)

    root.left = Node(8)
    root.right = Node(22)

    root.left.left = Node(4)
    root.left.right = Node(12)

    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    print(lca(root, 8, 14))
