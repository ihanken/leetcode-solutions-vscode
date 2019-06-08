#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0

        if not root.left and not root.right: return 1

        minChildDepth = float('inf')

        if root.left: minChildDepth = min(minChildDepth, self.minDepth(root.left))
        if root.right: minChildDepth = min(minChildDepth, self.minDepth(root.right))

        return 1 + minChildDepth

