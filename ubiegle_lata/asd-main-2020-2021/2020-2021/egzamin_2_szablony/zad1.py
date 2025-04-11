from zad1testy import runtests

def binary_search(tab, value):
    start = 0
    end = len( tab ) - 1
    while start <= end:
        middle = ( start + end ) // 2
        if value > tab[ middle ][0]: start = middle + 1
        else: end = middle - 1
    res=[]
    while start < len(tab) and tab[ start ][0] == value:
        res.append(start)
        start+=1
    return res


def intuse( I, x, y ):
    """tu prosze wpisac wlasna implementacje"""
    n=len(I)
    dp=[None for _ in range(n)]
    for i in range(n):
        I[i]=(I[i][0],I[i][1],i)
    I.sort()
    useful=[]
    def rek(ind):
        if dp[ind]!=None:
            return dp[ind]
        if I[ind][1]==y:
            useful.append(I[ind][2])
            return True
        l=binary_search(I,I[ind][1])
        if l==[]:
            dp[ind]=False
            return False
        flag=False
        for i in l:
            if rek(i):
                dp[i]=True
                useful.append(I[ind][2])
                flag=True
            else:
                dp[i]=False
        dp[ind]=flag
        return flag

    t=binary_search(I,x)
    for i in t:
        rek(i)
            
    return list(set(useful))



runtests( intuse )


