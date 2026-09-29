'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''

from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        # deque q and p as pair
        queue = deque([(q, p)]) 

        # while items are in the queue
        while queue:
            # curr1 = q, curr2 = p
            curr1, curr2 = queue.popleft()
            # go to the next iteration in the while loop if both curr1 and curr2 are null values
            if curr1 is None and curr2 is None:
                continue
            # if one is null and the other is not null this is not a same tree. return False
            if curr1 is None or curr2 is None:
                return False
            # if either curr1 or curr2 values don't match, this is not a same tree. return False
            if curr1.val != curr2.val:
                return False
            # enqueue curr1 and curr2 left as a pair and same for right 
            queue.append((curr1.left, curr2.left))
            queue.append((curr1.right, curr2.right))
        # return True if False is never reached
        return True
