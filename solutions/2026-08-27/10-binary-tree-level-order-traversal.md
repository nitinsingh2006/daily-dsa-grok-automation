# Binary Tree Level Order Traversal

**Difficulty:** Medium  
**Topic:** Trees

Return a list of node values level by level in a binary tree.

## Approach
Perform BFS using a queue to collect nodes per level.

## Complexity
O(n) time, O(n) space

## Solution
```python
def levelOrder(root):
    if not root:
        return []
    from collections import deque
    q = deque([root])
    res = []
    while q:
        level_size = len(q)
        level = []
        for _ in range(level_size):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res
```
