def initialiser(signal1, signal2):
  '''
  >>> initialiser([17.0, -8.5, -8.5], [-28.5, -28.5, 57.0])
  (3.3529411764705883, 2)
  >>> initialiser([10.82, 35.0, 10.82, -28.32, -28.32], [23.79, 77.0, 23.79, -62.29, -62.29])
  (2.2, 0)
  >>> initialiser([17.5, 35.0, 17.5, -17.5, -35.0, -17.5], [49.5, -49.5, -99.0, -49.5, 49.5, 99.0])
  (2.8285714285714287, 4)
  >>> initialiser([47.0, -47.0, -94.0, -47.0, 47.0, 94.0], [39.0, 19.5, -19.5, -39.0, -19.5, 19.5])
  (0.4148936170212766, 1)
  '''
  imax1 = imax2 = 0
  n = len(signal1)
  for i in range(1, n):
    if signal1[i]>signal1[imax1]:
      imax1 = i
    if signal2[i]>signal2[imax2]:
      imax2 = i
  phase = (imax2 if imax2>=imax1 else imax2+n) - imax1
  return (signal2[imax2]/signal1[imax1], phase)

import doctest
doctest.run_docstring_examples(initialiser, globals())
