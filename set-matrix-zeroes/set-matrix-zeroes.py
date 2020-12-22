class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        l=len(matrix)
        m=len(matrix[0])
        ans=[]
        for i in range(l):
            for j in range(m):
                if matrix[i][j]==0:
                    ans.append([i,j])
                    
        for k in range(len(ans)):
            pair=ans[k]
            x=pair[0]
            
            for j in range(len(matrix[0])):
                matrix[x][j]=0
                
            y=pair[1]
            for j in range(len(matrix)):
                matrix[j][y]=0
        return matrix
        """
        Do not return anything, modify matrix in-place instead.
        """
        
