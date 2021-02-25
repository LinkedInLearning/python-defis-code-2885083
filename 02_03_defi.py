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
  prec = extraire(echec, cases)
  while prec and cases:
    prec = extraire(echec, cases, prec)
  return prec!=()

def position_valide(pos):
  return 'a' <= pos[0] <= 'h' and '1' <= pos[1] <= '8'

def coordonnees(pos):
  return (ord(pos[0])-ord('a'), ord(pos[1])-ord('1'))

def extraire(echec, cases, prec=()):
  case = cases.pop(0)
  if not position_valide(case):
    return ()
  (x, y) = coordonnees(case)
  if echec[x][y] or prec and abs((prec[0]-x)*(prec[1]-y))!=2:
    return ()
  echec[x][y] = True
  return (x, y)

import doctest
doctest.run_docstring_examples(cavalier, globals())
