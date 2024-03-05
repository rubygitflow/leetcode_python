# https://leetcode.com/problems/linked-list-cycle/description/
# 141. Linked List Cycle

# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# Constraints:
# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

class Solution:
    def hasCycleTwoPointer(self, head: Optional[ListNode]) -> bool:
        ''' Code Two-Pointer '''
        slow_pointer = head
        fast_pointer = head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False
    def hasCycleHashTable(self, head: Optional[ListNode]) -> bool:
        ''' Code Hash Table '''
        visited_nodes = set()
        current_node = head
        while current_node:
            if current_node in visited_nodes:
                return True
            visited_nodes.add(current_node)
            current_node = current_node.next
        return False 

def add_linked_list(data, pos):
    tail = []
    tail.append(ListNode(data[0])) 
    for x in data[1:]:
        tail.append(ListNode(x)) # Create a node
    for i in range(len(data) - 1):
        tail[i].next = tail[i+1] # Move the tail pointer
    if pos >= 0:
        tail[len(data) - 1].next = tail[pos]
    return tail[0]

head = add_linked_list([3,2,0,-4], 1)
# Output: true
# head = add_linked_list([1,2], 0)
# Output: true
# head = add_linked_list([1], -1)
# Output: false

Solution().hasCycleTwoPointer(head)
Solution().hasCycleHashTable(head)
