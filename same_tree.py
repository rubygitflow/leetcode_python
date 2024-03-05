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


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

def create_node(to_node, data, is_left):
    if is_left:
        to_node.left = TreeNode(data)
        return to_node.left
    else:
        to_node.right = TreeNode(data)
        return to_node.right

def add_tree(data):
    if not data:
        return None
    root = TreeNode(data[0])
    if len(data) > 1:
        node1 = TreeNode(data[1])
        root.left = node1
    if len(data) > 2:
        node2 = TreeNode(data[2])
        root.right = node2
    if len(data) > 3:
        create_node(node1, data[3], True)
    if len(data) > 4:
        create_node(node1, data[4], False)
    if len(data) > 5:
        create_node(node2, data[5], True)
    if len(data) > 6:
        create_node(node2, data[6], False)
    return root

p, q = [1,2,3], [1,2,3]
# Output: true

p, q = [1,2], [1,None,2]
# Output: false

p, q = [1,2,1], [1,1,2]
# Output: false
Solution().isSameTree(add_tree(p), add_tree(q))

p = [1,2,2,3,4,4,3]
# Output: true
Solution().isSymmetric(add_tree(p))

# p = [1,2,2,None,3,None,3]
# Output: false
Solution().isSymmetric(add_tree(p))
