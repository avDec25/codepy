class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def areIdentical(T, S):
    if T is None and S is None: return True
    if T is None or S is None: return False

    return (
            T.val == S.val
            and areIdentical(T.left, S.left)
            and areIdentical(T.right, S.right)
    )


def isSubtree(T, S):
    if S is None: return True
    if T is None: return False

    if areIdentical(T, S):
        return True

    return areIdentical(T.left, S) or areIdentical(T.right, S)


if __name__ == "__main__":
    T = Node(26)
    T.right = Node(3)
    T.right.right = Node(3)
    T.left = Node(10)
    T.left.left = Node(4)
    T.left.left.right = Node(30)
    T.left.right = Node(6)

    S = Node(10)
    S.right = Node(6)
    S.left = Node(4)
    S.left.right = Node(30)

    if isSubtree(T, S):
        print("Tree S is subtree of Tree T")
    else:
        print("Tree S is not a subtree of Tree T")
