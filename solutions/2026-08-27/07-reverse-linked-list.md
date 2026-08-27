# Reverse Linked List

**Difficulty:** Medium  
**Topic:** Linked List

Reverse a singly linked list and return the new head node.

## Approach
Iteratively change next pointers while traversing the list.

## Complexity
O(n) time, O(1) space

## Solution
```python
def reverseList(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```
