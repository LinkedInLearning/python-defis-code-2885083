def perroquet(phrase, max_syllabes):
  '''
  >>> perroquet("Et maintenant quelque chose de complètement différent", 4)
  différent
  >>> perroquet("Snap snap, grin grin, wink wink, nudge nudge", 4)
  wink wink, nudge nudge
  >>> perroquet("Se défendre en cas d'attaque avec des fruits frais", 4)
  des fruits frais
  >>> perroquet("Que font-ils dans mon estomac ? Aucune idée, ils paient un loyer ?", 4)
  paient un loyer
  >>> perroquet("Python", 4)
  Python
  >>> perroquet("Python", 1)
  ""
  '''
  return 'argh'

import doctest
doctest.run_docstring_examples(perroquet, globals())