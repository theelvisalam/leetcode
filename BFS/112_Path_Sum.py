'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        # if tree has nothing in it return false
        if not root:
            return False
        
        # add root and sum as pair to q
        q = deque()
        q.append((root, 0))
        
        # while q is not empty
        while q:
            # get first item in q assign (curr = root, sum = 0)
            curr, sum = q.popleft()

            # add current value to sum
            sum += curr.val
            
            # if no left or right node means you're on a leaf then you can return True if the sum matches targetSum
            if not curr.left and not curr.right:
                if sum == targetSum:
                    return True
            # enqueue left and right nodes along with the current sum
            if curr.left:
                q.append((curr.left, sum))
            if curr.right:
                q.append((curr.right, sum))
        # if sum does not equal targetSum return False
        return False


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    # root.right = TreeNode(8)
    # root.left.left = TreeNode(11)
    # root.left.left.left = TreeNode(7)
    # root.left.left.right = TreeNode(2)
    # root.right.left = TreeNode(13)
    # root.right.right = TreeNode(4)
    # root.right.right.right = TreeNode(1)

    print(Solution().hasPathSum(root, 1))  # expected: False
