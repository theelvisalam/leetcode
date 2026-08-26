'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,5]

Example 2:
Input: list1 = [], list2 = [1,2]
Output: [1,2]

Example 3:
Input: list1 = [], list2 = []
Output: []
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        while list1 or list2:
            temp = 0
            curr1 = list1
            curr2 = list2

            if curr1 < curr2 and curr1 <= curr1.next:
                continue
            if curr1 < curr2:

            if curr2 < curr1:
                temp = curr1
                curr1 = curr2
                curr2 = curr1


        




list1 = build_linked_list([1,2,4])
list2 = build_linked_list([1,3,5])
sol = Solution()
print(sol.mergeTwoLists(list1, list2))

        
