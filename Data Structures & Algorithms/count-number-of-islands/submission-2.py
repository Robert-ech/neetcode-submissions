class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # nested for loop to traverse through the grid
        # for each one if its a 1, run bfs on it and then add 1 to counter
        # add all found 1s to a seen set using the grid coords
        # use Row Col to traverse grid
        def dfs(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return
            if grid[r][c] == '0' or (r,c) in seen:
                return
            
            seen.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
            

        seen = set()
        R,C = len(grid), len(grid[0])
        count = 0

        for r in range(R):
            for c in range(C):
                if (r,c) in seen or grid[r][c] == '0':
                    continue
                if grid[r][c] == '1':
                    dfs(r,c)
                    count += 1
        return count
