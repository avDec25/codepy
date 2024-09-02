class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def maxUtil(node):
    if node is None:
        return 0

    l_mx = maxUtil(node.left)   # left is solved: max path sum on left
    r_mx = maxUtil(node.right)  # right is solved: max path sum on right

    # should take max of two and the root, or just the root itself is max
    # maximum sum of: the path to left OR the path to right; from the root
    # either left child will make max, or right one,
    # or none and just the root itself is max alone,
    # without their help
    mx_single = max(node.val + max(l_mx, r_mx), node.val)

    # global update
    mx_top = max(mx_single, node.val + l_mx + r_mx)
    maxUtil.ans = max(maxUtil.ans, mx_top)

    return mx_single



def findMaxPathSum(node):
    maxUtil.ans = float("-inf")
    maxUtil(node)
    return maxUtil.ans


def maxPathSumNoRecursion(root):
    mx_sum = float("-inf")
    stack = []
    stack.append((root, 1))

    while stack:
        node, state = stack.pop()

        if node is None:
            continue

        if state == 1:
            stack.append((node, 2))
            stack.append((node.left, 1))
        elif state == 2:
            stack.append((node, 3))
            stack.append((node.right, 1))
        else:
            l_sum = node.left.val if node.left is not None else 0
            r_sum = node.right.val if node.right is not None else 0

            # global update
            # including the left max or right max, including the root
            # meaning max-path-sum in whole tree
            # in contrast to: just left path max, or right path max
            mx_sum = max(mx_sum, node.val + max(0, l_sum) + max(0, r_sum))
                                          # ^should we take left_sum or not

            # local updates
            mx_child_sum = max(l_sum, r_sum)
            node.val += max(0, mx_child_sum)
    return mx_sum


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)

    # root = Node(-25)
    # root.left = Node(3)
    # root.right = Node(4)

    print("Max path Sum = ", findMaxPathSum(root))
    print("No Recursion, Max path Sum = ", maxPathSumNoRecursion(root))
