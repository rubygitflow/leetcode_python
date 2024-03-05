# https://leetcode.com/problems/same-tree/description/
# 100. Same Tree

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:
# Input: p = [1,2], q = [1,None,2]
# Output: false
# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# Constraints:
# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104

# Approach
# 1. We start by checking if both trees are null. If they are, they are the same, so we return true.
# 2. If one of the trees is null and the other is not, they cannot be the same, so we return false.
# 3. If both trees are not null, we check if their values are equal.
# 4. Then, we recursively call the function on their left and right subtrees and check if they are the same.
# 5. We combine the results of the checks on the current node's value and its subtrees and return the final result.

#######################
# https://leetcode.com/problems/symmetric-tree/description/
# 101. Symmetric Tree
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,None,3,None,3]
# Output: false

# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100

#######################
# https://leetcode.com/problems/balanced-binary-tree/description/
# 110. Balanced Binary Tree

# Given a binary tree, determine if it is height-balanced

# Example 1:
# Input: root = [3,9,20,None,None,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,None,None,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true

# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

#######################
# https://leetcode.com/problems/path-sum/description/
# 112. Path Sum

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

# Example 1:
# Input: root = [5,4,8,11,None,13,4,7,2,None,None,None,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.

# Example 2:
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.

# Example 3:
# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.

# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000


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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_is_null = p is None
        q_is_null = q is None
        if p_is_null and q_is_null:
            return True
        elif p_is_null or q_is_null:
            return False
        else:
            status = p.val == q.val
            status &= self.isSameTree(p.left, q.left)
            status &= self.isSameTree(p.right, q.right)
            return status
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:        
        def dfs(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None or root1.val != root2.val:
                return False
            return dfs(root1.left, root2.right) and dfs(root1.right, root2.left)
        return dfs(root, root)
    def helper(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        # if parents are unbalanced, even children will be unbalanced
        if l == -1 or r == -1:
            return -1
        if abs(l - r ) > 1:
            return -1
        return 1 + max(l, r)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        output = self.helper(root)
        if output > -1:
            return True
        return False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        left_sum = self.hasPathSum(root.left, targetSum - root.val)
        right_sum = self.hasPathSum(root.right, targetSum - root.val)
        return left_sum or right_sum

def build_binary_tree(items: list[int]) -> TreeNode:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None
    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None
        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node
    return inner()

p, q = [1,2,3], [1,2,3]
# Output: true

p, q = [1,2], [1,None,2]
# Output: false

p, q = [1,2,1], [1,1,2]
# Output: false
Solution().isSameTree(
    build_binary_tree(p),
    build_binary_tree(q)
)

p = [1,2,2,3,4,4,3]
# Output: true
Solution().isSymmetric(build_binary_tree(p))

# p = [1,2,2,None,3,None,3]
# Output: false
Solution().isSymmetric(build_binary_tree(p))

p = [3,9,20,None,None,15,7]
# Output: true
p = [1,2,2,3,3,None,None,4,4]
# Output: false
p = []
# Output: true
Solution().isBalanced(build_binary_tree(p))

p, targetSum = [5,4,8,11,None,13,4,7,2,None,None,None,1], 22
# Output: true
p, targetSum = [1,2,3], 5
# Output: false
p, targetSum = [], 0
# Output: false
Solution().hasPathSum(build_binary_tree(p), targetSum)
