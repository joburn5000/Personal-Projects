'''
Given the head of a sorted linked list, delete all duplicates such that 
each element appears only once. Return the linked list sorted as well.

Completed: 12/08/2021
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None: return head
        curr = head
        while (curr.next):
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else: curr = curr.next
        return head
