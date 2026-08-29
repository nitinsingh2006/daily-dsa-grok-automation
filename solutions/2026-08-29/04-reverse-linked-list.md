# Reverse Linked List

**Difficulty:** Medium  
**Topic:** Linked Lists

Reverse a singly linked list and return the new head.

## Approach
Iterative pointer reversal.

## Complexity
O(n) time, O(1) space

## Solution
```python
def reverseList(head):prev=None;curr=head;while curr:nxt=curr.next;curr.next=prev;prev=curr;curr=nxt;return prev
```
