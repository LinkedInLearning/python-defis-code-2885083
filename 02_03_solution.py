TAILLE = 8

def cavalier(trajet):
  '''
  >>> cavalier('x4')
  False
  >>> cavalier('a9')
  False
  >>> cavalier('d4')
  True
  >>> cavalier('d4 d5')
  False
  >>> cavalier('d4 c6')
  True
  >>> cavalier('d4 c6 d4')
  False
  >>> cavalier('d4 c6 b4 d3 e5')
  True
  '''
  echec = [([False] * TAILLE).copy() for i in range(TAILLE)]
  cases = trajet.split(' ')
  prec = ()
  while cases:
    x, y = coordonnees(cases.pop(0))
    if not limite(x) or not limite(y) or echec[x][y] or prec and not atteint(x, y, prec):
      return False
    echec[x][y] = True
    prec = (x, y)
  return True

def atteint(x, y, dest):
  return abs((dest[0]-x)*(dest[1]-y))==2

def limite(v):
  return 0 <= v <TAILLE

def coordonnees(pos):
  return (ord(pos[0])-ord('a'), ord(pos[1])-ord('1'))

import doctest
doctest.run_docstring_examples(cavalier, globals())
