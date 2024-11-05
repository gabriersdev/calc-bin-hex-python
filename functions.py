def binToDec(nBin) :
  somatoria = 0
  for pos in range(len(str(nBin))):
    #   Base para conversão é 2
    somatoria += int(str(nBin)[pos]) * (2 ** (len(str(nBin)) - 1 - pos))
  return somatoria

def decToBin(nDec):
  sequencia = ''
  resto = 0
  i = 0
  quociente = int(nDec)

  # Enquanto quociente não for zero, bloco roda
  while quociente != 0:
    # Obtém o resto da divisão pela base, que é 2
    resto = quociente % 2
    sequencia += str(resto)
    quociente //= 2

  ret = list(sequencia)
  ret.reverse()
  ret = ''.join(ret)
  return ret

  # Ou
  # return bin(nDec)[2:]

def hexToDec(nHex):
  tCorrespond = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
  aHex = str(nHex).upper()
  somatoria = 0
  for i, char in enumerate(aHex): # Usar enumerate para obter índice e valor
    val = tCorrespond.get(char, char)  # Obter valor da tabela ou manter o próprio char se não for letra
    somatoria += int(val) * (16 ** (len(aHex) - 1 - i)) # Converter para int somente no cálculo
  return somatoria

def decToHex(nDec):
  return hex(nDec)[2:].upper()
