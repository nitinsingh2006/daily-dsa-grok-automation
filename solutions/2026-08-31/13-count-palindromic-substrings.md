# Count Palindromic Substrings

**Difficulty:** Medium  
**Topic:** Strings

Given a string, count all substrings that are palindromes.

## Approach
Expand around each center to count palindromes in O(n^2) time.

## Complexity
O(n^2) time, O(1) space

## Solution
```python
def count_palindromes(s):\n    n=len(s)\n    count=0\n    for center in range(2*n-1):\n        left=center//2\n        right=left+center%2\n        while left>=0 and right<n and s[left]==s[right]:\n            count+=1\n            left-=1\n            right+=1\n    return count
```
