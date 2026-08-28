# Cycle Detection

**Difficulty:** Hard  
**Topic:** Graphs

Given a directed graph as an adjacency list, determine if it contains a cycle.

## Approach
Perform DFS with a recursion stack to detect back edges.

## Complexity
O(V+E) time, O(V) space

## Solution
```python
def has_cycle(adj):
    visited = set()
    rec_stack = set()
    def dfs(v):
        visited.add(v)
        rec_stack.add(v)
        for nei in adj.get(v, []):
            if nei not in visited:
                if dfs(nei):
                    return True
            elif nei in rec_stack:
                return True
        rec_stack.remove(v)
        return False
    for node in adj:
        if node not in visited:
            if dfs(node):
                return True
    return False
```
