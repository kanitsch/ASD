from zad7testy import runtests

def maze( L ):
    n=len(L)
    D=[[[-1,-1] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        if can_move_to(L,i,0):
            D[i][0][1]=i
        else: break
    for col in range(1,n):
        for row in range(n):
            m=max(D[row][col-1])
            if m!=-1 and can_move_to(L,row,col):
                D[row][col]=[m+1,m+1]
        for row in range(1,n):
            if can_move_to(L,row,col) and D[row-1][col][1]!=-1:
                D[row][col][1]=max(D[row][col][1],D[row-1][col][1]+1)
        for row in range(n-2,-1,-1):
            if can_move_to(L,row,col) and D[row+1][col][0]!=-1:
                D[row][col][0]=max(D[row][col][0],D[row+1][col][0]+1)
    return max(D[n-1][n-1])

def can_move_to(L,x,y):
    return L[x][y]!='#'

def mymaze(L):
    n=len(L)
    d=[[[-1,-1] for _ in range(n)]for _ in range(n)]
    for row in range(n):
        if L[row][0]=='#':
            break
        d[row][0][1]=row # 1 oznacza że wchodzimy od góry lub z lewej, 0 - od dołu lub lewej
    for col in range(1,n):
        for row in range(n):
            if L[row][col]!='#':
                m=max(d[row][col-1])
                if m!=-1:
                    d[row][col]=[m+1,m+1]
        for row in range(1,n):
            if L[row][col]!='#' and d[row-1][col][1]!=-1:
                d[row][col][1]=max(d[row][col][1],d[row-1][col][1]+1)
        for row in range(n-2,-1,-1):
            if L[row][col]!='#' and d[row+1][col][0]!=-1:
                d[row][col][0]=max(d[row][col][0],d[row+1][col][0]+1)
    return max(d[n-1][n-1])
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mymaze, all_tests = True )