from BinaryTree import *

if __name__ == "__main__":
    head= TreeNode(1)
    head.left= TreeNode(2)
    head.right= TreeNode(3)
    head.left.left= TreeNode(4)
    head.left.right= TreeNode(5)
    head.right.left= TreeNode(6)
    head.right.right= TreeNode(7)
    print(head)
    pass