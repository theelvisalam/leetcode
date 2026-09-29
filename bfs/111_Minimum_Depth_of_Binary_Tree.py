'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
'''

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # if root is blank return min depth of 0
        if not root:
            return 0
        
        # create a q
        q = deque()
        # append as a pair - root and depth
        q.append((root, 1))
        
        # while q is not empty
        while q:
            # get next item in q, curr = root, depth = 'number'
            curr, depth = q.popleft()
            # if on this iteration there is no left or right, that means you're done return depth
            if not curr.left and not curr.right:
                return depth
            # if current iteration has a left node, append left node to q and append depth incremented up by one 
            if curr.left:
                q.append((curr.left, depth + 1))
            # same as left, but for right
            if curr.right:
                q.append((curr.right, depth + 1))

        # return depth calcualted by while loop
        return depth
                    

                    
    
                
                
                
                