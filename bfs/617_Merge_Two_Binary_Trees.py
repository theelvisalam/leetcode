'''
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.
'''

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # Check for blank trees, if both non existent return nothing, if one is null return the other
        if not root1 and not root2:
            return None
        if not root1:
            return root2
        if not root2:
            return root1
        
        # deque root1 and roo2 as a pair
        q = deque([(root1, root2)])

        # while items are in the q
        while q:
            # curr1 = root1, curr2 = root2, popleft first value of each root
            curr1, curr2 = q.popleft()
            # store all addition of curr values into root1
            curr1.val += curr2.val
            # if both left nodes of the current iteration are not null, append both items into q as a pair
            if curr1.left and curr2.left:
                q.append((curr1.left, curr2.left))
            # since everything is being stored onto root1, if root1 left node is null, replace it with root2 left node
            elif not curr1.left:
                curr1.left = curr2.left
            # if both roots right nodes are not null, append both right nodes into q as a pair
            if curr1.right and curr2.right:
                q.append((curr1.right, curr2.right))
            # last check, if the root1 right node is null, replace it with root2 right node, same as what is being done for the left node
            elif not curr1.right:
                curr1.right = curr2.right
        # everything is stored onto root1, return root1
        return root1



        