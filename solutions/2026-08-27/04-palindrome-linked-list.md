# Palindrome Linked List

**Difficulty:** Medium  
**Topic:** Linked List

Determine if a singly linked list is a palindrome.

## Approach
Reverse second half and compare.

## Complexity
O(n) time, O(n) space

## Solution
```python
def is_palindrome(head):\n    vals=[]\n    while head:\n        vals.append(head.val)\n        head=head.next\n    return vals==vals[::-1]
```
