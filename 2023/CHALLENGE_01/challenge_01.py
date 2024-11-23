
from collections import defaultdict


def leer_fichero ( filename: str ) -> str:
  message = ''
  with open( filename ) as file:
    message = file.readline()
  
  return message
  

def descifrar_mensaje ( message: str ) -> str:
  words = defaultdict(int)
  
  for word in message.split():
    words[word.lower()] += 1
  
  return ''.join( f'{word}{count}' for word, count in words.items() )  
  

if __name__ == '__main__':
  
  message = leer_fichero( './message_01.txt' )
  print(descifrar_mensaje(message))
  