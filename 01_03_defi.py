fromages = {
  "France": {
    "Brebis": {
      "Fromage frais": {
        "Brocciu": 0
      },
      "Pâte persillée": { 
        "Roquefort": 0
      },
      "Pâte pressée": {
        "Non cuite": { 
          "Ossau-iraty": 0
        }
      }
    },
  	"Chèvre": {
      "Fromage frais": {
        "Brocciu": 0,
        "Brousse du Rove": 0
      },
      "Pâte molle": {
        "Croûte fleurie": {
          "Banon": 0, 
          "Rigotte de Condrieu": 0
        },
        "Croûte naturelle": {
          "Chabichou du Poitou": 0,
          "Charolais": 0,
          "Crottin de Chavignol": 0,
          "Mâconnais": 0,
          "Pélardon": 0,
          "Picodon": 0,
          "Pouligny-saint-pierre": 0,
          "Rocamadour": 0,
          "Sainte-maure-de-touraine": 0,
          "Selles-sur-cher": 0,
          "Valençay": 0
        }
      },
      "Pâte pressée": {
        "Non cuite": { 
          "Chevrotin": 0 
        }
      }
    },
    "Vache": {
      "Pâte molle": { 
        "Croûte fleurie": {	
          "Brie de Meaux": 0,
          "Brie de Melun": 0,
          "Camembert de Normandie": 0,
          "Chaource": 0,
          "Neufchâtel": 0
        },
        "Croûte lavée": {
          "Époisses": 0,
          "Langres": 0,
          "Livarot": 0,
          "Maroilles ou marolles": 0,
          "Mont d'Or": 0,
          "Munster": 0,
          "Pont-l'évêque": 0
        }
      },
      "Pâte persillée": {
        "Bleu d'Auvergne": 0,
        "Bleu de Gex": 0,
        "Bleu des Causses": 0,
        "Bleu du Vercors-Sassenage": 0,
        "Fourme d'Ambert": 0,
        "Fourme de Montbrison": 0
      },
      "Pâte pressée": {
        "Cuite": {
          "Abondance": 0,
          "Beaufort": 0,
          "Comté": 0,
        },
        "Non cuite": {	
          "Cantal": 0,
          "Laguiole": 0,
          "Morbier": 0,
          "Reblochon": 0,
          "Saint-nectaire": 0,
          "Salers": 0,
          "Tome des Bauges": 0,
        }
      }
    }
  }
}

def trouver(criteres):
  '''
  >>> trouver('')
  47
  >>> trouver('spam')
  0
  >>> trouver('Cantal')
  1
  >>> trouver('Pâte pressée')
  12
  >>> trouver('Pâte pressée, Spam')
  0
  >>> trouver('Non cuite, Vache')
  7
  >>> trouver('Vache, Non cuite')
  7
  '''
  return -1

import doctest
doctest.run_docstring_examples(trouver, globals())