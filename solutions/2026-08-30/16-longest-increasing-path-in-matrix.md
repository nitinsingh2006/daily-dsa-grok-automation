# Longest Increasing Path in Matrix

**Difficulty:** Hard  
**Topic:** DFS

Given a matrix of integers, find the length of the longest strictly increasing path.

## Approach
DFS with memoization to avoid recomputation.

## Complexity
O(m*n) time, O(m*n) space

## Solution
```python
def longestIncreasingPath(matrix):
    if not matrix: return 0
    m, n = len(matrix), len(matrix[0])
    memo = [[0]*n for _ in range(m)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def dfs(i,j):
        if memo[i][j]: return memo[i][j]
        best = 1
        for di,dj in dirs:
            ni, nj = i+di, j+dj
            if 0<=ni<m and 0<=nj<n and matrix[ni][nj]>matrix[i][j]:
                best = max(best, 1+dfs(ni,nj))
        memo[i][j] = best
        return best
    res = 0
    for i in range(m):
        for j in range(n):
            res = max(res, dfs(i,j))
    return res
```
