class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n  = len(grid) , len(grid[0])
        
        
        def magic(a, b, c, d, e, f, g, h, i):
            return (set([a, b, c, d, e, f, g, h, i]) == set(range(1, 10)) and (a+b+c == d+e+f == g+h+i == a+d+g == b+e+h == c+f+i == a+e+i == c+e+g))
        
        ans = 0
        for r in range(m - 2):
            for c in range(n - 2):
                if magic(grid[r][c], grid[r][c+1], grid[r][c+2], grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2], grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]):
                    ans += 1
                    
        return ans
