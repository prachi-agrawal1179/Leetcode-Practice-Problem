class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        output=[[1]]
        for i in range(1,numRows):
            res=[1]
            for j in range(1,i):
                res.append(output[i-1][j-1]+output[i-1][j])
            res.append(1)
            output.append(res)
        return output
            
        
