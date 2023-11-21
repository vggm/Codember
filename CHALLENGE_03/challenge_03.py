

def seperar_politica ( politica: str ) -> (int,int,str):
  partes = politica.split()
  min_max = partes[0].split('-')
  return int(min_max[0]), int(min_max[1]), partes[1]
  
  
def es_valida ( fila: str ) -> bool:
  politica_clave = fila.split(':')
  politica, clave = politica_clave[0], politica_clave[1]
  
  minimo, maximo, caracter = seperar_politica( politica )
  
  return minimo <= clave.count(caracter) <= maximo


def leer_fichero ( filename: str ) -> None:
  
  with open(filename) as file:
    i = 1
    line = file.readline()
    while line != '':
      
      if not es_valida(line):
        if i in [13, 42]:
          print(f'{i}. {line.split()[-1]}')
        i += 1
      
      line = file.readline()


if __name__ == '__main__':
  
  leer_fichero('./message_03.txt')