message = "PGMQBZWBZKKOJWPMMGBXWGGDBANXSJMXKZLJEPGKCHOAQOGOZJQVZMTOJWJVGVBXVEWOQBWVPJKVGZMQXAUKWDZZKESXPQBQPPPXFOMRAVMQNCAIBSXOJVKW"

def lapin_de_troie(msg):
  return "???"

def envoyer_le_lapin(lapin, msg):
  while len(msg) > 24:
    msg = lapin( msg )
  return msg

print(envoyer_le_lapin(lapin_de_troie, message))