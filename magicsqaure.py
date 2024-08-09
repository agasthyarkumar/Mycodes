class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(i, j):
            s = set()
            for x in range(3):
                for y in range(3):
                    if grid[i + x][j + y] < 1 or grid[i + x][j + y] > 9:
                        return False
                    s.add(grid[i + x][j + y])
            if len(s) != 9:
                return False

            return (grid[i][j] + grid[i][j + 1] + grid[i][j + 2] == 
                    grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2] == 
                    grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2] == 
                    grid[i][j] + grid[i + 1][j] + grid[i + 2][j] == 
                    grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1] == 
                    grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2] == 
                    grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] == 
                    grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j])

        rows, cols = len(grid), len(grid[0])
        count = 0
        
        for i in range(rows - 2):
            for j in range(cols - 2):
                if grid[i + 1][j + 1] == 5 and isMagic(i, j):
                    count += 1
                    
        return count
