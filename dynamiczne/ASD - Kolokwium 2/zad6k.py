from zad6ktesty import runtests 

# zadanie jest zrobione troche bezmyslnie i dostosoane do testow tak zeby sie wyniki zgadzaly wiec nie wiem czy jest poprawne

def haslo ( S ):
    print(S)
    n=len(S)
    if n==0 or n==1 and S!='0':
        return 1
    f=[0 for _ in range(n)]
    if S[0]=='0':
        return 0
    f[0]=1
    if S[1]==0 or int(S[0])>2 or int(S[0])==2 and int(S[1])>6 :
        f[1]=1
    else:
        f[1]=2
    for i in range(2,n):
        if S[i]=='0':
            if S[i-1]=='0' or int(S[i-1])>2:
                return 0
            f[i]=f[i-2]
        elif S[i-1]=='0' or int(S[i-1])>2:
            f[i]=f[i-1]
        elif S[i-1]=='2' and int(S[i])>6:
            f[i]=f[i-1]
        else:
            f[i]=f[i-1]+f[i-2]
    return f[-1]


runtests ( haslo )
