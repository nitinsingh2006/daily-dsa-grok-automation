# Count Palindromic Substrings

**Difficulty:** Medium  
**Topic:** Strings

Given a string, count all substrings that read the same forwards and backwards.

## Approach
Expand around each center to find palindromes.

## Complexity
O(n^2) time, O(1) space

## Solution
```python
def count_palindromes(s):\n    n=len(s)\n    count=0\n    for i in range(n):\n        l=r=i\n        while l>=0 and r<n and s[l]==s[r]:\n            count+=1\n            l-=1\n            r+=1\n        l=i\n        r=i+1\n        while l>=0 and r<n and s[l]==s[r]:\n            count+=1\n            l-=1\n            r+=1\n    return count
```
