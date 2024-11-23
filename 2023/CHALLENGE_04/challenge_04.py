from collections import defaultdict

def contar_caracters ( nombre: str ) -> dict:
  memo = defaultdict(int)
  for c in nombre:
    memo[c] += 1
  return memo


def calcular_checksum( nombre: str ) -> str:
  counter = contar_caracters(nombre)
  return ''.join( c for c in counter if counter[c] == 1 )
  

def checksum_valido ( archivo: str ) -> bool:
  nombre, checksum = archivo.split('-')
  return calcular_checksum(nombre) == checksum


def leer_fichero ( filename: str ) -> None:
  
  with open( filename ) as file:
    index = 1
    line = file.readline().removesuffix('\n')
    while line != '':
      
      if checksum_valido( line ):
        if index == 33:
          print(f"33. {line.split('-')[1]}")       
        index += 1 
      
      line = file.readline().removesuffix('\n')
      

if __name__ == '__main__':
  leer_fichero( './files_quarantine.txt' )
  