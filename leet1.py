class Solution:
    def findTheCity(self, N: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF=10**20
        d=[[INF] * N for _ in range(N)]
        for i in range(N):
            d[i][i]=0
        for u,v,w in edges:
            d[u][v]=w
            d[v][u]=w
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    d[i][j]=min(d[i][j],d[i][k] + d[k][j])
        bestcity=None
        bestreach=INF
        for i in range(N):
            reach=0
            for j in range(N):
                if d[i][j]<=distanceThreshold:
                    reach+=1
            if reach<=bestreach:
                bestcity=i
                bestreach=reach
        return bestcity
