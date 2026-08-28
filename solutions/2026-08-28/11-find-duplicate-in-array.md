# Find Duplicate in Array

**Difficulty:** Medium  
**Topic:** Arrays

Given an array of n+1 integers where each integer is between 1 and n inclusive, find the duplicate number. The array contains only one duplicate, but it may appear more than once.

## Approach
Use Floyd's Tortoise and Hare cycle detection to find the duplicate without extra space.

## Complexity
O(n) time, O(1) space

## Solution
```python
def find_duplicate(nums):
    slow = nums[0]
    fast = nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
```
