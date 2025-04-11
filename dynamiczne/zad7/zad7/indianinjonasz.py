from zad7testy import runtests
        
 
def rek(L,d,n,x,y,dir,vis):
    if x<0 or y<0 or y==n:
        return - float('inf')
    if vis[y][x][dir]:
        return d[y][x][dir]
    if L[y][x]=='#':
        vis[y][x]=[True,True]
        return -1
    if dir==0:
        d[y][x][0]=max(rek(L,d,n,x-1,y,0,vis),rek(L,d,n,x-1,y,1,vis),rek(L,d,n,x,y-1,0,vis))
        if d[y][x][0]!=-1:
            d[y][x][0]+=1
    if dir==1:
        d[y][x][1]=max(rek(L,d,n,x-1,y,0,vis),rek(L,d,n,x-1,y,1,vis),rek(L,d,n,x,y+1,1,vis))
        if d[y][x][1]!=-1:
            d[y][x][1]+=1
    vis[y][x][dir]=True
    return d[y][x][dir]

def maze( L ):
    n=len(L)
    d=[[[-1,-1] for _ in range(n)] for _ in range(n)]
    i=0
    vis=[[[False,False] for _ in range(n)] for _ in range(n)]
    while i<n and L[i][0]=='.':
        d[i][0][0]=i
        vis[i][0]=[True,True]
        i+=1
    while i<n:
        vis[i][0]=[True,True]
        i+=1
    return max(rek(L,d,n,n-1,n-1,0,vis),rek(L,d,n,n-1,n-1,1,vis))
    
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )