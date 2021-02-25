from enum import Enum

voyelles = "aâeéêèioôu"
espaces = " \t\n\r?!,.:;^"

def perroquet(phrase_init, max_syllabes):
  '''
  >>> perroquet("Et maintenant quelque chose de complètement différent", 4)
  'différent'
  >>> perroquet("Snap snap, grin grin, wink wink, nudge nudge", 4)
  'wink wink, nudge nudge'
  >>> perroquet("Se défendre en cas d'attaque avec des fruits frais", 4)
  'des fruits frais'
  >>> perroquet("Que font-ils dans mon estomac ? Aucune idée, au moins, ils paient un loyer ?", 4)
  'paient un loyer ?'
  >>> perroquet("Grenouilles croquantes glacées au glucose", 7)
  'croquantes glacées au glucose'
  >>> perroquet("Python", 4)
  'Python'
  >>> perroquet("Python", 1)
  ''
  '''
  phrase = '^'+phrase_init.lower()
  etat = etat_intervalle
  debut = len(phrase)
  syllabes = 0
  for indice in reversed(range(len(phrase))):
    etat, inc, debut_mot = etat(phrase[indice])
    syllabes += inc
    if syllabes > max_syllabes:
      break
    if debut_mot:
      debut = indice + 1

  return phrase_init[debut-1:]

def etat_intervalle(lettre):
  return (etat_pluriel_emuet, 0, False) if lettre=='s' \
    else traiter_mot(lettre, False)
  
def etat_voyelles(lettre):
  return traiter_lettre(lettre, 0, True)

def etat_consonnes(lettre):
  return traiter_lettre_consonne(lettre, True)

def etat_pluriel_emuet(lettre):
  return traiter_mot(lettre, False)

def etat_emuet(lettre):
  return (etat_voyelles  , 1, False) if lettre in voyelles \
    else (etat_intervalle, 1, True ) if lettre in espaces \
    else (etat_emuet     , 0, False)

def traiter_lettre(lettre, inc_voyelle, mot):
  return (etat_voyelles  , inc_voyelle, False) if lettre in voyelles \
    else (etat_intervalle,           0, mot  ) if lettre in espaces \
    else (etat_consonnes ,           0, False)

def traiter_lettre_consonne(lettre, mot):
  return (etat_voyelles, 1, False) if lettre=='y' \
    else traiter_lettre(lettre, 1, mot)

def traiter_mot(lettre, mot):
  return (etat_emuet, 0, False) if lettre == 'e' \
    else traiter_lettre_consonne(lettre, mot)

import doctest
doctest.run_docstring_examples(perroquet, globals())
