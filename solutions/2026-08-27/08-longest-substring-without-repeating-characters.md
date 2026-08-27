# Longest Substring Without Repeating Characters

**Difficulty:** Hard  
**Topic:** Strings

Find the length of the longest substring without repeating characters.

## Approach
Use a sliding window and a set to track seen characters.

## Complexity
O(n) time, O(min(n, m)) space

## Solution
```python
def lengthOfLongestSubstring(s):
    seen = {}
    left = 0
    max_len = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```
