from zad3testy import runtests
'''
def N(T):
    n=0
    while T!=None:
        T=T.left
        n+=1
    return 2**n

def T_array(T,A,i=1):
    if T!=None:
        A[i]=T.key
        T_array(T.left,A,2*i)
        T_array(T.right,A,2*i+1)


def maxim( T, C ):
    """tu prosze wpisac wlasna implementacje"""
    n=N(T) 
    A=[0 for _ in range(n)]
    T_array(T,A)
    best=-float('inf')
    for c in C:
        best=max(best,A[c])
    return best

    
runtests( maxim )'''


def find_node(root, idx):
    current = root
    # Ominięcie najstarszego bitu, bo odpowiada za korzeń
    bit_length = idx.bit_length() - 2
    
    while bit_length >= 0:
        # Jeśli bit jest ustawiony na 1, idziemy w prawo
        if idx & (1 << bit_length):
            current = current.right
        # W przeciwnym razie idziemy w lewo
        else:
            current = current.left
        bit_length -= 1
    
    return current

def maxim(T, X):
    max_value = float('-inf')
    for idx in X:
        node = find_node(T, idx)
        max_value = max(max_value, node.key)
    return max_value


runtests( maxim )

