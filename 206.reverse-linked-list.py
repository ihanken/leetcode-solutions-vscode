#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None

        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current
        
        return prev

        

