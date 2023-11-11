
OPERACIONES = {
  '#': lambda x: x + 1,
  '@': lambda x: x - 1,
  '*': lambda x: x * x,
  '&': lambda x: print(x, end='')
}

def compilar_mensaje ( mensaje: str ) -> str:
  numero_oculto = 0
  for c in mensaje:
    value = OPERACIONES[c](numero_oculto)
    if value is not None:
      numero_oculto = value
    
  return numero_oculto


def leer_fichero ( fichero: str ) -> str:
  mensaje = ''
  with open( fichero ) as f:
    mensaje = f.readline()
  return mensaje


if __name__ == '__main__':
  mensaje = leer_fichero ( './message_02.txt' )
  # print(mensaje)
  compilar_mensaje(mensaje)