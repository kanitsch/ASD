from egzP1atesty import runtests 

def titanic( W, M, D ):
    #tutaj proszę wpisać własną implementację
    stri=''
    for i in W:
        stri+=(M[ord(i)-ord('A')][1])
    for i in range(len(D)):
        D[i]=(len(M[D[i]][1]),M[D[i]][1])
    D.sort(reverse=True)
    cnt=[float('inf') for _ in range(len(stri))]
    cnt[0]=1
    for i in range(2,5):
        for el in D:
            if el[1]==stri[:i]:
                cnt[i-1]=1
    for i in range(len(stri)):
        for el in D:
            if i+el[0]<len(stri):
                if el[1]==stri[i+1:i+1+el[0]]:
                    cnt[i+el[0]]=min(cnt[i+el[0]],cnt[i]+1) 
    return cnt[len(stri)-1]      
                    
                
        
    return 0

runtests ( titanic, recursion=False )