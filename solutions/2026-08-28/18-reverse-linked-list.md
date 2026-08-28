# Reverse Linked List

**Difficulty:** Medium  
**Topic:** Linked Lists

Reverse a singly linked list and return the new head.

## Approach
Iteratively rewire next pointers using three pointers: prev, curr, next.

## Complexity
O(n) time, O(1) space

## Solution
```python
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def reverse_list(head):
    prev=None
    curr=head
    while curr:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt
    return prev
```
