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
for i in range(0, 20):
  for j in range(len(personnages)):
    iterations += 1
    if etapes[j] and etapes[j][0][0] == i:
      etape, action = etapes[j].pop(0)
      print(i+1, personnages[j], ':', action)
      break

print()
print(iterations, 'itérations')