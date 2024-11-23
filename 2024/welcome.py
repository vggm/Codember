

def resolve(num: str, secuencia: str) -> int:
  candado = [int(x) for x in num]
  n = len(candado)
  
  pos = 0
  for movimiento in secuencia:
    match movimiento:
      case 'R':
        pos = (pos + 1) % n
      case 'L':
        pos = (pos - 1) % n
      case 'U':
        candado[pos] = (candado[pos] + 1) % 10
      case 'D':
        candado[pos] = (candado[pos] - 1) % 10
  
  return ''.join(str(x) for x in candado)
        
  


if __name__ == '__main__':
  print(resolve('000', 'URURD'))
  print(resolve('1111', 'UUURUUU'))
  print(resolve('9999', 'LULULULD'))
  
  print('\nRETO 1:')
  print(resolve('528934712834', 'URDURUDRUDLLLLUUDDUDUDUDLLRRRR'))