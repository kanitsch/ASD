from egzP7btesty import runtests 
	
# akceptowalna

def ogrod( S, V ):
    #Tutaj proszę wpisać własną implementację
    n=len(S)
    maxi=0
    for j in range(n):
        tab=[0 for _ in range(n)]
        zysk=0
        for i in range(j,n):
            if tab[S[i]-1]==1:
                zysk-=V[S[i]-1] 
                tab[S[i]-1]=-1
            elif tab[S[i]-1]==0:
                zysk+=V[S[i]-1]
                tab[S[i]-1]=1
            maxi=max(maxi,zysk)
            
    return maxi
    
runtests(ogrod, all_tests = True)