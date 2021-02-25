def tri_votes(votes):
  '''
  >>> tri_votes([])
  []
  >>> tri_votes([1, 0])
  [0, 1]
  >>> tri_votes([2, 1])
  [1, 2]
  >>> tri_votes([0, 0, 0])
  [0, 0, 0]
  >>> tri_votes([1, 1, 1])
  [1, 1, 1]
  >>> tri_votes([2, 2, 2])
  [2, 2, 2]
  >>> tri_votes([1, 1, 0])
  [0, 1, 1]
  >>> tri_votes([2, 1, 0, 1, 0, 1, 2, 0, 1, 1, 0, 2, 2, 1, 0, 1, 1, 0])
  [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]
  '''  
  return votes

import doctest
doctest.run_docstring_examples(tri_votes, globals())