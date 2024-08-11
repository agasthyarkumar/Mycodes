class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def isDisconnected(grid):
            def dfs(i, j):
                if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                    return
                grid[i][j] = 0
                for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    dfs(i + x, j + y)

            found_island = False
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        if found_island:
                            return True  # More than one island found
                        found_island = True
                        dfs(i, j)
            return not found_island  # Return True if no islands are found

        # If already disconnected
        if isDisconnected([row[:] for row in grid]):
            return 0

        # Try removing each land cell to see if it disconnects the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if isDisconnected([row[:] for row in grid]):
                        return 1
                    grid[i][j] = 1

        return 2
