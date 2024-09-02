class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def hasSameStructure(r1, r2):
    if r1 is None and r2 is None:
        return True

    if r1 is not None and r2 is not None:
        return (hasSameStructure(r1.left, r2.left)) and (hasSameStructure(r1.right, r2.right))

    return False


root1 = Node(10)
root2 = Node(100)

root1.left = Node(7)
root1.right = Node(15)

root1.left.left = Node(4)
root1.left.right = Node(9)
root1.right.right = Node(20)

root2.left = Node(70)
root2.right = Node(150)

root2.left.left = Node(40)
root2.left.right = Node(90)
root2.right.right = Node(200)

if (hasSameStructure(root1, root2)):
    print("Both trees have same structure")
else:
    print("Trees do not have same structure")
