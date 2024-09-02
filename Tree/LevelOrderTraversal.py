from collections import deque


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def bfs(root):
    q = deque()
    q.append(root)

    while q:
        for _ in range(len(q)):
            node = q.popleft()
            print(f"{node.val}", end=', ')

            if node.right is not None:
                q.append(node.right)

            if node.left is not None:
                q.append(node.left)
        print("\n")


def dfs(root):
    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        print(node.val, end=", ")

        if node.right is not None:
            stack.append(node.right)

        if node.left is not None:
            stack.append(node.left)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(12)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)

    print("dfs: ")
    dfs(root)

    print("\n\nbfs: ")
    bfs(root)
