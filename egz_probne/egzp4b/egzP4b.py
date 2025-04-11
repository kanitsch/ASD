from egzP4btesty import runtests 

class Node:
  def __init__(self, key, parent):
    self.left = None
    self.right = None
    self.parent = parent
    self.key = key
    self.x = None
  
def prev(x):
  if x.left:
    x=x.left
    while x.right !=None:
      x=x.right
  else:
    sz=x.key
    while x.key>=sz:
      x=x.parent
  return x.key

def next(x):
  if x.right:
      x=x.right
      while x.left !=None:
        x=x.left
  else:
      sz=x.key
      while x.key<=sz:
        x=x.parent
  return x.key
    

def sol(root, T):
  suma=0
  for el in T:
    l=prev(el)
    p=next(el)
    if el.key*2==l+p:
      
      suma+=el.key

    
  return suma
    
runtests(sol, all_tests = True)