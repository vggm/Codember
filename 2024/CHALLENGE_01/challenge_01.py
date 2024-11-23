

def get_line(file: str):
  with open(file, 'r') as rfile:
    line = rfile.readline().removesuffix('\n')
    while line != '':
      yield line
      line = rfile.readline().removesuffix('\n')


def is_attempt(word: str):
  lower_limit = 0
  for ascii_code in list(map(ord, word)):
    
    if ascii_code < lower_limit:
      return False
    
    if 48 <= ascii_code <= 57: # number:
      lower_limit = ascii_code
    
    elif 97 <= ascii_code <= 122: # lower letter
      lower_limit = ascii_code

  return True


def resolve():
  t, f = 0, 0
  for line in get_line('./log.txt'):
    if is_attempt(line):
      t += 1
    else:
      f += 1
  
  print(f"{t}true{f}false")


if __name__ == '__main__':
  resolve()
  # print(is_attempt('ijpx'))