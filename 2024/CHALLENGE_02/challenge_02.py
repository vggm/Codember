

def get_lines(file: str):
  with open(file, 'r') as rfile:
    line = rfile.readline().removesuffix('\n')
    while line != '':
      yield line
      line = rfile.readline().removesuffix('\n')


def steps_to_escape(arr: list[int]) -> int:
  
  steps, pos = 0, 0
  while 0 <= pos < len(arr):
    arr[pos], pos = arr[pos] + 1, pos + arr[pos]
    steps += 1  
    
  return steps


def resolve():
  total_sum, last = 0, 0
  for line in get_lines('./trace.txt'):
    last = steps_to_escape(list(map(int, line.split())))
    total_sum += last
  
  print(f"{total_sum}-{last}")


if __name__ == '__main__':
  resolve()
  