from egzP6btesty import runtests 

def move(y,x,s):
    if s[0]=='L':
        x-=2
    elif s[0]=='R':
        x+=2
    elif s[0]=='U':
        y+=2
    elif s[0]=='D':
        y-=2
    if s[1]=='L':
        x-=1
    elif s[1]=='R':
        x+=1
    elif s[1]=='U':
        y+=1
    elif s[1]=='D':
        y-=1
    return (y,x)

def jump ( M ):
    #tutaj proszę wpisać własną implementację
    y=0
    x=0
    lights={(0,0):True}
    cnt=1
    for jump in M:
        (y,x)=move(y,x,jump)
        if (y,x) in lights:
            if lights[(y,x)]==True:
                lights[(y,x)]=False
                cnt-=1
            else:
                lights[(y,x)]=True
                cnt+=1
        else:
            lights[(y,x)]=True
            cnt+=1
    #cnt=0
    #for key in lights:
    #    if lights[key]==True:
    #        cnt+=1
    return cnt
    
runtests(jump, all_tests = True)