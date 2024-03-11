# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description/
# 298. Binary Tree Longest Consecutive Sequence

# Given the root of a binary tree, return the length of the longest consecutive sequence path.
# A consecutive sequence path is a path where the values increase by one along the path.
# Note that the path can start at any node in the tree, and you cannot go from a node to its parent in the path.

# Example 1:
# Input: root = [1,None,3,2,4,None,None,None,5]
# Output: 3
# Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

# Example 2:
# Input: root = [2,None,3,2,None,1]
# Output: 2
# Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.

# Constraints:
# The number of nodes in the tree is in the range [1, 3 * 104].
# -3 * 104 <= Node.val <= 3 * 104

#######################
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/description/
# 549. Binary Tree Longest Consecutive Sequence II

# Given the root of a binary tree, return the length of the longest consecutive path in the tree.
# A consecutive path is a path where the values of the consecutive nodes in the path differ by one. This path can be either increasing or decreasing.
# For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid.
# On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

# Example 1:
# Input: root = [1,2,3]
# Output: 2
# Explanation: The longest consecutive path is [1, 2] or [2, 1].

# Example 2:
# Input: root = [2,1,3]
# Output: 3
# Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].

# Constraints:
# The number of nodes in the tree is in the range [1, 3 * 104].
# -3 * 104 <= Node.val <= 3 * 104

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return f"val: {self.val}, left: {self.left}, right: {self.right}"
    def __str__(self) -> str:
        return str(self.val)

from typing import Optional

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        max_arr = 0
        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            # количество в глубину с текущим уровнем
            l = dfs(root.left) + 1
            r = dfs(root.right) + 1
            # сброс количества в глубину, если не соблюдается "последовательность"
            if root.left and root.left.val - root.val != 1:
                l = 1
            if root.right and root.right.val - root.val != 1:
                r = 1
            # выбираем максимальную ветку
            t = max(l, r)
            nonlocal max_arr
            # фиксируем максимальную глубину
            max_arr = max(max_arr, t)
            # print('root.val, l, r, t, max_arr',root.val, l, r, t, max_arr)
            return t
        dfs(root)
        return max_arr
    def longestConsecutiveII(self, root: Optional[TreeNode]) -> int:
        pass


def build_binary_tree(items: list[int]) -> TreeNode:
    """ Create BT from list of values. """
    n = len(items)
    if n == 0:
        return None
    def inner(index: int = 0) -> TreeNode:
        """ Closure function using recursion bo build tree """
        if n <= index or items[index] is None:
            return None
        # print('index, n, items[index]',index, n, items[index])
        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node
    return inner()

p = [1,None,3,None,None,2,4,None,None,None,None,None,None,None,5]
# Output: 3
p = [2,None,3,None,None,2,None,None,None,None,None,1,None]
# Output: 2
Solution().longestConsecutive(build_binary_tree(p))

p = [1,2,3]
# Output: 2
p = [2,1,3]
# Output: 3
Solution().longestConsecutiveII(build_binary_tree(p))
