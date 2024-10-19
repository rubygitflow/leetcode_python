# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self) -> str:
        return f"val: {self.val}, next: {self.next}"
    def __str__(self) -> str:
        s = '['
        s += str(self.val)
        node = self.next
        while node:
            s += ','
            s += str(node.val)
            node = node.next
        s += "]"
        return s

# creation a linked list from data with closure at pos
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
