# Min Depth of Binary Tree - Python Interview Question(Recursion)


# define a Class Tree, to initiate the binary tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def height_binary_tree(root):

    if root is None:
        return 0
    else:
        lheight = height_binary_tree(root.left)
        rheight = height_binary_tree(root.right)

        return min(lheight, rheight) + 1


# Test the algorithm
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)

print("Height of the binary tree is: " + str(height_binary_tree(root)))
