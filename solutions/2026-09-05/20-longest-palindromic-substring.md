# Longest Palindromic Substring

**Difficulty:** Medium  
**Topic:** Strings

Find longest palindromic substring in a given string.

## Approach
Expand around center for each index.

## Complexity
O(n^2) time, O(1) space

## Solution
```python
def longest_palindrome(s):
    if not s: return ''
    start=0;end=0
    for i in range(len(s)):
        l=i;r=i
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1;r+=1
        l+=1;r-=1
        if r-l+1>end-start+1:
            start=l;end=r
        l=i;r=i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1;r+=1
        l+=1;r-=1
        if r-l+1>end-start+1:
            start=l;end=r
    return s[start:end+1]
```
