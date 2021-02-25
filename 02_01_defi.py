personnages = [
  "Client-e", 
  "Maître-sse d'hôtel", 
  "Chef-fe",
  "Serveuse/serveur", 
]
etapes = [
  [ [  0, "Se présenter" ],
    [  3, "Choisir" ],
    [  5, "Signaler une fourchette sale" ],
    [  9, "Donner son choix" ],
    [ 14, "Manger" ],
    [ 16, "Demander l'addition" ],
    [ 18, "Payer" ],
    [ 19, "Partir" ]
  ],
  [ [  1, "Conduire à la table" ],
    [  2, "Donner une carte" ],
    [  4, "Renseigner le client" ],
    [  6, "S'excuser " ],
    [  7, "Remplacer par une fourchette propre" ],
    [  8, "Commencer la prise de commande" ],
    [ 10, "Transmettre en cuisine" ],
    [ 17, "Amener l'addition" ]
  ],
  [ [ 11, "Préparer les plats" ],
    [ 12, "Indiquer la disponibilité" ]
  ],
  [ [ 13, "Servir le plat" ],
    [ 15, "Débarrasser" ]
  ],
]

iterations = 0
i = 0
j = 0
while i < 20:
  for k in range(len(etapes[j])):
    iterations += 1
    etape, action = etapes[j][k]
    if etape < i:
      continue
    if etape > i:
      break
    print(i+1, personnages[j], ':', action)
    i += 1
  j = (j + 1) % len(personnages)

print()
print(iterations, "itérations")