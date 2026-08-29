# Longest Consecutive Sequence in Linked List

**Difficulty:** Medium  
**Topic:** Linked List

Given the head of a singly linked list of integers, find the length of the longest consecutive sequence of values (each value differs by 1 from its predecessor). Return the maximum length.

## Approach
Traverse the list while tracking current run length. Reset when the difference is not 1. Keep a maximum variable. Complexity O(n).

## Complexity
O(n) time, O(1) space

## Solution
```python
def longest_consecutive(head):
    if not head:
        return 0
    max_len=cur_len=1
    prev=head.val
    node=head.next
    while node:
        if node.val==prev+1:
            cur_len+=1
        else:
            cur_len=1
        if cur_len>max_len:
            max_len=cur_len
        prev=node.val
        node=node.next
    return max_len
```
