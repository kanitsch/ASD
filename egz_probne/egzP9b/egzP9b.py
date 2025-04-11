'''from egzP9btesty import runtests

def takieuler(G):
    def DFS_Visit(G,u,odp):
        for i in range(len(G[u])):
            v=G[u][i]
            G[u][i]='eee'
            if v!='eee':
              DFS_Visit(G,v,odp)
        odp.append(u)
    n=len(G)
    odp=[]
    DFS_Visit(G,0,odp)
    odp.reverse()
    return odp

def czynne(G,R):
    for u in range(len(R)):
        for v in R[u]:
            G[u].remove(v)
    return G

def dyrektor( G, R ):
	#Tutaj proszę wpisać własną implementację
	C=czynne(G,R)
	return takieuler(C)
	
runtests(dyrektor, all_tests=True)'''

from egzP9btesty import runtests

def takieuler(G):
        stack = [0]
        path = []
        current_edge = [0 for _ in range (len(G))]  # to keep track of which edge we are exploring for each vertex
        
        while stack:
            u = stack[-1]
            if current_edge[u] < len(G[u]):
                v = G[u][current_edge[u]]
                current_edge[u] += 1
                stack.append(v)
            else:
                path.append(stack.pop())
        
        return path[::-1]  # return reversed path



def czynne(G, R):
    #G_copy = [adj_list.copy() for adj_list in G]  # Deep copy of the graph
    for u in range(len(R)):
        for v in R[u]:
            if v in G[u]:
                G[u].remove(v)

def dyrektor(G, R):
    czynne(G, R)
    return takieuler(G)

runtests(dyrektor, all_tests=True)



