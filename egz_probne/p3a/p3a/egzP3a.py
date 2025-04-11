from egzP3atesty import runtests
from math import inf

class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None
    
def glosy(node):
  p=node
  cnt=0
  while p!=None:
    p=p.next
    cnt+=1
  tab=[[0 for _ in range(node.fundusze+1)] for _ in range(cnt)]
  tab[0][node.koszt]=node.wyborcy
  node=node.next
  for i in range (1,cnt):
    ko=node.koszt
    wy=node.wyborcy
    for j in range(node.fundusze+1):
      tab[i][j]=tab[i-1][j]
      if j-ko>=0:
        tab[i][j]=max(tab[i-1][j],tab[i-1][j-ko]+wy)
    node=node.next
  return max(tab[cnt-1])
    

def wybory(T):
    #tutaj proszę wpisać własną implementację
    suma=0
    for wyb in T:
      suma+=glosy(wyb)
    return suma

runtests(wybory, all_tests = True)