class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, matrix):
        directions = [(0 ,1) , (0, -1) , (1 , 0) ,(-1 , 0)]
        #  connected --> BFS 
        # do 2 fbs (red / blue)
        # count number of cells that can touch 2 lakes  
        R ,C = len(matrix) , len(matrix[0])
        colors = [[0]*C for i in range(R)]
        def bfs(curr):
            visited = set()
            while curr :
                temp = []
                for r  , c in curr :
                    if (r , c) in visited :
                        continue
                    if (r , c) not in visited :
                        visited.add((r , c))
                        colors[r][c] += 1
                        for dx , dy in directions :
                            new_dx = dx + r 
                            new_dy = dy + c 
                            if 0 <= new_dx < C and 0 <= new_dy < R :
                                temp.append((new_dx , new_dy))
                curr = temp 
            return 
        curr = []
        for r in range(R):
            curr.append((r , 0))
        for c in range(C):
            curr.append((0 , c))
        bfs(curr)
        curr = []
        for r in range(R):
            curr.append((r , C-1))
        for c in range(C):
            curr.append((R-1 , c))
        bfs(curr)
        
        ans = 0
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 2 :
                    ans += 1
        return ans  
        