class Solution(object):
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        inf=10**20
        alpha=26
        distance=[[inf]*alpha for _ in range(alpha)]
        for s,t,c in zip(original, changed, cost):
            u=ord(s)-ord('a')
            v=ord(t)-ord('a')
            distance[u][v]=min(distance[u][v],c)
        for k in range(alpha):
            for i in range(alpha):
                for j in range(alpha):
                    distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])
                    total=0
        for s,t in zip(source, target):
            if s==t:
                continue
            u=ord(s)-ord('a')
            v=ord(t)-ord('a')
            if distance[u][v]>=inf:
                return -1
            total+=distance[u][v]
        return total
