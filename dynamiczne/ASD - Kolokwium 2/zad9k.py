from zad9ktesty import runtests
from math import inf

def wjazd(P,i,g,d):
    if i==len(P):
        return i-1
    if g<0 or d<0:
        return i-1
    return max(wjazd(P,i+1,g-P[i+1],d),wjazd(P,i+1,g,d-P[i+1]))

def f(P,dp,i,g,d):
    if i==len(P):
        return 0
    if dp[i][g][d]!=-1:
        return dp[i][g][d]
    if P[i]>g and P[i]>d:
        dp[i][g][d]=0
        return 0
    if P[i]>g:
        dp[i][g][d]=f(P,dp,i+1,g,d-P[i])+1
    elif P[i]>d:
        dp[i][g][d]=f(P,dp,i+1,g-P[i],d)+1
    else:
        dp[i][g][d]=max(f(P,dp,i+1,g-P[i],d),f(P,dp,i+1,g,d-P[i]))+1
    return dp[i][g][d]
    
        

def prom(P, g, d):
    dp=[[[-1 for _ in range(d+1)] for _ in range(g+1) ] for _ in range(len(P))]
    i=f(P,dp,0,g,d)-1
    l1=[]
    l2=[]
    flag=False
    for i in range(len(P)-1):
        if g-P[i]>=0 and dp[i][g][d]==dp[i+1][g-P[i]][d]+1>0:
            l1.append(i)
            last=l1
            g-=P[i]
        elif d-P[i]>=0 and dp[i][g][d]>0:
            l2.append(i)
            last=l2
            d-=P[i]
        else:
            flag=True
            break
    if not flag:
        if g-P[-1]>=0:
            l1.append(len(P)-1)
            last=l1
        elif d-P[-1]>=0:
            l2.append(len(P)-1)
            last=l2            
    return last

runtests ( prom )