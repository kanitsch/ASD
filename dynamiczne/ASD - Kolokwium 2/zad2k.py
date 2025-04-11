from zad2ktesty import runtests

def parz(S,i,j):
    cnt=0
    while i>=0 and j<len(S) and S[i]==S[j]:
        cnt+=2
        i-=1
        j+=1

    napis=S[i+1:j]
    return cnt, napis

def nieprz(S,i,j):
    cnt=1
    while i>=0 and j<len(S) and S[i]==S[j]:
        cnt+=2
        i-=1
        j+=1
    napis=S[i+1:j]
    return cnt, napis

def palindrom( S ):
    #Tutaj proszę wpisać własną implementację
    maxx=0
    maxnap=''
    for i in range(1,len(S)):
        cnt,nap=nieprz(S,i-1,i+1)
        if cnt>maxx:
            maxx,maxnap=cnt,nap
        if S[i-1]==S[i]:
            cnt,nap=parz(S,i-1,i)
            if cnt>maxx:
                maxx,maxnap=cnt,nap
    return maxnap

runtests ( palindrom )