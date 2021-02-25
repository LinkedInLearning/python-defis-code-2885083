ref = { 
  "a": [ "autorite"    , 0, "Les experts sont unanimes.", "Il y a des voix dissonantes." ],
  "b": [ "bonnefoi"    , 0, "Nous avons toujours été guidés par le désir de bien faire.", "L'enfer est pavé de bonnes intentions." ],
  "c": [ "comparaison" , 2, "Si c'est valable pour {0}, rien n'empêche de le considérer pour {1}.", "Comparaison n'est pas raison ! On ne peut assimiler {0} et {1}." ],
  "d": [ "definition"  , 2, "{0} c'est d'abord {1}.", "{0} c'est bien autre chose." ],
  "e": [ "extreme"     , 1, "Et pourquoi pas {0}, tant que vous y êtes !.", "Inutile d'exagérer !." ],
  "f": [ "afortiori"   , 2, "Si c'est valable pour {0} ça l'est à plus forte raison aussi pour {1}.", "Oui, mais il y a des solutions plus adaptées." ],
  "g": [ "gaspi"       , 1, "Ça fera économiser beaucoup de {0}.", "Il y a d'autres moyens d'en économiser." ],
  "h": [ "adhominem"   , 2, "Vous prônez {0} mais ça ne vous empêche pas de {1}.", "Il y a des choses qui ont plus d'impact sur {0}." ],
  "i": [ "incompatible", 1, "On ne peut comprendre que si l'on est {0}.", "Cela peut aussi faire perdre son objectivité." ],
  "j": [ "justice"     , 0, "On ne peut faire aucune exception.", "Il le faut, les conditions de départ sont différentes." ],
  "l": [ "alternative" , 2, "Il faut choisir : soit {0}, soit {1}.", "Le monde n'est pas tout blanc ou tout noir, une troisième piste est envisageable." ],
  "m": [ "forcemajeur" , 0, "Il n'y a aucune autre méthode éprouvée.", "Tout n'a pas encore été essayé." ],
  "n": [ "narration"   , 1, "Vous connaissez {0}, vous vous rappelez comment ça se termine.", "Ici, c'est la vraie vie, pas une fiction." ], 
  "o": [ "opportunité" , 0, "C'est vraiment le bon moment, toutes les conditions sont réunies.", "Il ne faut pas confondre vitesse et précipitation." ],
  "p": [ "adpersonam"  , 0, "Vous êtes mal placé pour dire ça.", "Au contraire, je suis plus que légitime." ],
  "q": [ "quantité"    , 0, "C'est ce que demande la majorité.", "On est toujours minoritaire quand on ouvre la voie." ],
  "r": [ "reciprocité" , 2, "On ne peut {0} d'un côté sans {1} de l'autre.", "On peut tout à fait, il y bien d'autres effets bénéfiques." ], 
  "s": [ "sacrifice"   , 0, "Ça a demander un effort considérable.", "Ne fallait-il pas vérifier avant si le jeu en valait vraiment la chandelle." ]
}
# prog --adhominem "l'économie d'énergie/rouler en 4x4" -ic "sur le terrain" "les smartphones/les ordinateurs"
argv = [
    "--adhominem", "l'économie d'énergie/rouler en 4x4",
    "-ic", "sur le terrain", "les smartphones/les ordinateurs"
]

# Affichage attendu :
# Vous prônez l'économie d'énergie mais ça ne vous empêche pas de rouler en 4x4.
# Il y a des choses qui ont plus d'impact sur l'économie d'énergie.

# On ne peut comprendre que si l'on est sur le terrain.
# Cela peut aussi faire perdre son objectivité.

# Si c'est valable pour les smartphones, rien n'empêche de le considérer pour les ordinateurs.
# Comparaison n'est pas raison ! On ne peut assimiler les smartphones et les ordinateurs.

def usage():
  print("Usage: prog -x [arguments]")
  for cmd, infos in ref.items():
    texte = str(infos[1]) + " argument(s)" if infos[1]>0 else "aucun argument"
    print("-" + cmd + ", --" + infos[0] + ": " + texte )

usage()

# Solution
cmds = []
errs = []

def traiter(cmd, params):
  if len(params) == ref[cmd][1]:
    for i in range(2, 4):
      print(ref[cmd][i].format(*params))
    print()
  else:
    errs.append(
      "L'argument de " + cmd + " doit être composé de " 
      + ref[cmd][1] + " partie(s) séparée(s) par des '/'."
    )

def interpreter(cmd):
  if cmd not in ref:
    errs.append("Commande '" + cmd + "' inconnue.")  
  elif ref[cmd][1]==0:
    traiter(cmd, [])
  else:
    cmds.append(cmd)  

def retrouver(complet):
  for cmd, infos in ref.items():
    if infos[0]==complet:
      interpreter(cmd)
      return
  errs.append("Commande '" + complet + "' inconnue.")

for arg in argv:
  if arg[0]=='-':
    if arg[1]=='-':
      retrouver(arg[2:])
    else:
      for cmd in arg[1:]:
        interpreter(cmd)
  elif cmds:
    traiter(cmds.pop(0), arg.split('/'))
  else:
    errs.append("Format de commande incorrect.")

if cmds:
  errs.append("Arguments manquants pour la/les commande(s) : "+', '.join(cmds)+".")
if errs:
  for e in errs:
    print(e)
  usage()