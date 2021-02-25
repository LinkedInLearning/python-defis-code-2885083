def rassembler(etages):
  '''
  >>> rassembler([0, 0, 0])
  []
  >>> rassembler([0, 1, 1])
  [(0, 1)]
  >>> rassembler([1, 0, 2])
  [(0, 2), (1, 2)]
  >>> rassembler([1, 0, 1, 2])
  [(1, 0), (1, 2), (0, 1), (0, 2), (1, 2)]
  >>> rassembler([0, 0, 2, 1, 2, 0])
  [(2, 1), (0, 2), (0, 1), (2, 1), (2, 0), (1, 2), (1, 0), (2, 0), (1, 2), (0, 1), (0, 2), (1, 2), (1, 0), (2, 0), (2, 1), (0, 1), (2, 0), (1, 2), (1, 0), (2, 0)]
  '''
  deplacements = []
  rassembler_rec(etages, len(etages), etages[-1], deplacements)
  return deplacements

def rassembler_rec(etages, taille, destination, deplacements):
  if taille:    
    indice_dernier = taille-1
    source = etages[indice_dernier]
    if source != destination:
      autre = 3-source-destination
      rassembler_rec(etages, indice_dernier, autre, deplacements)
      deplacements.append((source, destination))
      etages[indice_dernier] = destination
    rassembler_rec(etages, indice_dernier, destination, deplacements)

import doctest
doctest.run_docstring_examples(rassembler, globals())