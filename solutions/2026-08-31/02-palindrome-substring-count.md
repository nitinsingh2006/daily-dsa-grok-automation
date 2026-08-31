# Palindrome Substring Count

**Difficulty:** Medium  
**Topic:** Strings

Count all palindromic substrings in a given string.

## Approach
Expand around each center to find palindromes.

## Complexity
O(n^2) time, O(1) space

## Solution
```python
def solve(s):\n    n=len(s)\n    count=0\n    for center in range(2*n-1):\n        l=center//2\n        r=l+center%2\n        while l>=0 and r<n and s[l]==s[r]:\n            count+=1\n            l-=1\n            r+=1\n    return count
```
