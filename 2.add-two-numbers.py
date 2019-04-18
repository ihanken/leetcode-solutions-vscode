#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (30.74%)
# Total Accepted:    831.8K
# Total Submissions: 2.7M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1
        carry = 0

        while l1:
            l1.val += carry + (l2.val if l2 else 0)

            carry = l1.val // 10
            l1.val = l1.val % 10

            if not l1.next and l2:
                l1.next = l2.next
                l2 = None

            if not l1.next and carry > 0:
                l1.next = ListNode(carry)
                l1 = l1.next

            l1 = l1.next

            if l2: l2 = l2.next

        return head

