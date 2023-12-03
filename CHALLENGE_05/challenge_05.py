

class Usuario:
  def __init__(self, user_from_csv: str) -> None:
    
    partes = user_from_csv.split(',')
    
    self.id = partes[0]
    self.username = partes[1]
    self.email = partes[2]
    self.age = partes[3]
    self.location = partes[4]
    self.valid = True
    
    self._verificar_campos()
  
  def _verificar_campos (self) -> None:
    
    ''' Verificar que id, username y email no este vacio '''
    if not self.id or not self.username or not self.email:
      self.valid = False
      return
    
    ''' Verificar que id es alfanumerico '''
    if not self.id.isalnum():
      self.valid = False
      return
    
    ''' Verificar que username es alfanumerico '''
    if not self.username.isalnum():
      self.valid = False
      return
    
    ''' Verificar que age sea numerico '''
    if self.age != '':
      if not self.age.isnumeric():
        self.valid = False
      else: self.age = int(self.age)
    
    ''' Verificar que el email es valido '''
    self._verificar_email()
    
  
  def _verificar_email(self) -> None:
    if '@' not in self.email:
      self.valid = False
      return
    
    partes_del_email = self.email.split('@')
    if len(partes_del_email) > 2 \
      or partes_del_email[0] == '' or partes_del_email[1] == '':
      self.valid = False
      return
    
    if partes_del_email[1].count('.') == 0:
      self.valid = False


def leer_fichero ( filename: str ) -> None:
  with open(filename) as file:
    line = file.readline().removesuffix('\n')
    while line != '':
      
      user = Usuario(line)
      if not user.valid:
        dato = ''
        if len(user.username) > 0:
          dato = user.username[0]
        print(dato, end='')
      
      line = file.readline().removesuffix('\n')
  

if __name__ == '__main__':
  leer_fichero('./database_attacked.txt')
      