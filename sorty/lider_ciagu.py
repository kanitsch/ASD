def lider(l): #raczej nie o to chodzi w tym zadaniu
    n=len(l)
    s={}
    for i in range(n):
        if l[i] in s:
            s[l[i]]+=1
        else:
            s[l[i]]=1
    for i in range(n):
        if s[l[i]]>n//2:
            return True
    return False

l=[3,5,3,9,23,4,5,7,5,3,9,3]
print(lider(l))