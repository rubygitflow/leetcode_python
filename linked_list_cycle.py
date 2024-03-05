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

##########################
# https://leetcode.com/problems/add-two-numbers/description/
# 2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

##########################
# https://leetcode.com/problems/reverse-linked-list/
# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ''' Add Two Numbers '''
        dummyHead = ListNode(0)
        carry, tail = 0, dummyHead
        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0
            sum = digit1 + digit2 + carry
            carry, digit = divmod(sum, 10)
            # digit = sum % 10
            # carry = sum // 10
            tail.next = ListNode(digit)
            tail = tail.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        result = dummyHead.next
        dummyHead.next = None
        return result
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ''' Reverse Linked List '''
        new_list = None
        current = head
        while current:
            next_node = current.next
            current.next = new_list
            new_list = current
            current = next_node
        return new_list


def add_linked_list(data, pos = -1):
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

#########
# l1, l2 = [9,9,9,9,9,9,9], [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

l1, l2 = [2,4,3], [5,6,4]
# Output: [7,0,8]
res = Solution().addTwoNumbers(
    add_linked_list(l1),
    add_linked_list(l2)
)
# ...
res.val
res = res.next

#########
head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
res = Solution().reverseList(add_linked_list(head))
# ...
res.val
res = res.next
