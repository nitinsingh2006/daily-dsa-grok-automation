# Longest Palindromic Substring

**Difficulty:** Medium  
**Topic:** Strings

Given a string, find the longest contiguous substring that is a palindrome. Return the substring itself. If multiple substrings have the same maximum length, return the first one encountered.

## Approach
Expand around each center to check palindromes.

## Complexity
O(n^2) time, O(1) space

## Solution
```python
def solve(s):
    n=len(s)
    if n==0:return''
    start=0;end=0
    for i in range(n):
        l=i;r=i
        while l>=0 and r<n and s[l]==s[r]:
            l-=1;r+=1
        if r-l-1>end-start:
            start=l+1;end=r
        l=i-1;r=i+1
        while l>=0 and r<n and s[l]==s[r]:
            l-=1;r+=1
        if r-l-1>end-start:
            start=l+1;end=r
    return s[start:end]
```
