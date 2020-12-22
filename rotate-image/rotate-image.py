class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        from collections import deque
        m = len(matrix)
        n = len(matrix[0])
        queue = deque()
        for i in matrix:
            queue.appendleft(list(i))
        for i in range(n):
            for j in range(m):
                matrix[j][i] = queue[i][j]
                  
​
        """
        Do not return anything, modify matrix in-place instead.
        """
        
