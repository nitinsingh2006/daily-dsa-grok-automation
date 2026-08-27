# Reverse Linked List

**Difficulty:** Easy  
**Topic:** Linked Lists

Reverse a singly linked list in place.

## Approach
Iteratively reverse pointers.

## Complexity
O(n) time, O(1) space

## Solution
```python
def reverse_list(head):
    prev=None
    while head:
        nxt=head.next
        head.next=prev
        prev=head
        head=nxt
    return prev
```
