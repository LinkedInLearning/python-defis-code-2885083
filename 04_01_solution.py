def reordonner(t, indices, val, inc):
  if t[indices[1]] != val:
    return False
  tmp = t[indices[val]];
  t[indices[val]] = t[indices[1]]
  t[indices[1]] = tmp
  indices[val] += inc
  return True

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
  indices=[0, 0, len(votes)-1]
  while indices[1] <= indices[2]:
    if not reordonner(votes, indices, 2, -1):
      reordonner(votes, indices, 0, +1)
      indices[1]+=1
  return votes

import doctest
doctest.run_docstring_examples(tri_votes, globals())