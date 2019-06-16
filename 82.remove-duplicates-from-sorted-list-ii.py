#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextNodeIsDuplicate(self, head: ListNode) -> ListNode:
        return head and head.next and head.next.val == head.val

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = pre = ListNode(0)
        dummy.next = head

        while head and head.next:
            if head.val == head.next.val:
                while self.nextNodeIsDuplicate(head):
                    head = head.next
                    
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next

        return dummy.next
