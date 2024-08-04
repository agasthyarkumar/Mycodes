class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        inf=10**20
        cycle=change*2
        adj=collections.defaultdict(list)
        for u,v in edges:
            u-=1
            v-=1
            adj[u].append(v)
            adj[v].append(u)
        dist1=[inf]*n
        dist2=[inf]*n
        dist1[0]=0
        dist2[0]=inf
        h=[]
        heapq.heappush(h,(0,0,0))
        while len(h)>0:
            d, node, index =heapq.heappop(h)
            if index==0 and dist1[node]>d:
                continue
            if index==1 and dist2[node]>d:
                continue
            if index==1 and node==n-1:
                return d
            if d%cycle<change:
                nd=d+time
            else:
                    nd=((d+cycle-1)//cycle)*cycle+time
            for v in adj[node]:
                if nd<dist1[v]:
                    dist2[v]=dist1[v]
                    dist1[v]=nd
                    heapq.heappush(h,(nd,v,0))
                elif nd>dist1[v] and nd<dist2[v]:
                    dist2[v]=nd
                    heapq.heappush(h,(nd,v,1))
        assert(false)
        return -1
