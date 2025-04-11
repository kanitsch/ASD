def bellman_ford(G,s):
    n=len(G)
    d=[float('inf') for _ in range(n)]
    parent=[None for _ in range(n)]
    d[s]=0
    for _ in range(n-1):
        for u in range(n):
            for (v, d_uv) in G[u]:
                if d[v]>d[u]+d_uv:
                    d[v]=d[u]+d_uv
    for u in range(n):
        for (v, d_uv) in G[u]:
            if d[v]>d[u]+d_uv:
                print("cykl o ujemnej wadze")
                return -1
    return d
