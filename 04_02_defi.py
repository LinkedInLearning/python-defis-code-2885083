import random

etages = [random.randrange(3) for i in range(5)]

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
  return []

import doctest
doctest.run_docstring_examples(rassembler, globals())
