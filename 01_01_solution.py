message = "PGMQBZWBZKKOJWPMMGBXWGGDBANXSJMXKZLJEPGKCHOAQOGOZJQVZMTOJWJVGVBXVEWOQBWVPJKVGZMQXAUKWDZZKESXPQBQPPPXFOMRAVMQNCAIBSXOJVKW"

def lapin_de_troie(msg):
  return "???"

def envoyer_le_lapin(lapin, msg):
  while len(msg) > 24:
    msg = lapin( msg )
  return msg

def suppr(message, indice):
  return message.replace(message[indice], '')

def lapin_tueur(message):
  return suppr(suppr(message, 0), -1)

print(envoyer_le_lapin(lapin_tueur, message))