# Reverse Linked List

**Difficulty:** Medium  
**Topic:** Linked Lists

Reverse a singly linked list. Return the new head of the reversed list. Each node contains an integer value and a next pointer.

## Approach
Iteratively reverse pointers using three variables.

## Complexity
O(n) time, O(1) space

## Solution
```python
def reverseList(head):
    prev=None
    curr=head
    while curr:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt
    return prev
```
