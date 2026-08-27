# Longest Substring Without Repeating Characters

**Difficulty:** Hard  
**Topic:** Strings

Given a string, find the length of the longest substring without repeating characters.

## Approach
Sliding window with a hash map to track last seen indices.

## Complexity
O(n) time, O(min(n,alphabet)) space

## Solution
```python
def lengthOfLongestSubstring(s):
    seen={}
    left=0
    maxlen=0
    for right,ch in enumerate(s):
        if ch in seen and seen[ch]>=left:
            left=seen[ch]+1
        seen[ch]=right
        maxlen=max(maxlen,right-left+1)
    return maxlen
```
