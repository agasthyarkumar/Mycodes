class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = list(range(4 * n * n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY

        for r in range(n):
            for c in range(n):
                root = 4 * (r * n + c)
                val = grid[r][c]
                
                # Union the 4 triangles within the current cell
                if val != '/':
                    union(root + 0, root + 1)
                    union(root + 2, root + 3)
                if val != '\\':
                    union(root + 0, root + 3)
                    union(root + 1, root + 2)

                # Union the current cell with the right and bottom cells
                if c + 1 < n:
                    union(root + 1, 4 * (r * n + c + 1) + 3)
                if r + 1 < n:
                    union(root + 2, 4 * ((r + 1) * n + c) + 0)

        # Count the number of connected components
        return sum(parent[i] == i for i in range(4 * n * n))
