from collections import defaultdict


def resolve(network: list[list[int]]):
  nodes = set()
  childs = set()
  graph = defaultdict(list)
  parent = defaultdict(list)
  for org, dst in network:
    nodes.add(org)
    nodes.add(dst)
    childs.add(dst)
    graph[org].append(dst)
    parent[dst].append(org)
    
  roots = nodes - childs
  leafs = {c for c in childs if len(graph[c]) == 0 and len(parent[c]) == 1}
  
  sol = []
  for node in roots:
    child = graph[node][0]
    if child in leafs:
      sol += [node, child]
      
  return sorted(sol)
  
  
if __name__ == '__main__':
  test1 = [[1, 2], [2, 3], [4, 5]]
  test2 = [[1, 2], [2, 3], [3, 4]]
  test3 = [[4, 6], [7, 9], [10, 12], [12, 16]]
  problem = [[1,2],[2,3],[2,4],[3,4],[4,6],[5,6],[6,8],[7,8],[8,10],[9,10],[10,12],[11,12],[13,14],[15,16],[17,18],[19,20],[21,22],[23,24],[25,26],[27,28],[31,32],[33,34],[35,36],[37,38],[39,40],[41,42],[43,44],[45,46],[47,48],[49,50],[71,72],[73,74],[75,76],[77,78],[79,80],[81,82],[83,84],[85,86],[87,88],[155,156],[157,158],[175,176],[177,178],[179,180],[181,182],[183,184],[195,196],[197,198],[198, 199],[199,200]]
  
  sol1 = resolve(test1)
  assert sol1 == [4, 5], f"Expected [4, 5], got {sol1}"
  
  sol2 = resolve(test2)
  assert sol2 == [], f"Expected [], got {sol2}"
  
  sol3 = resolve(test3)
  assert sol3 == [4, 6, 7, 9], f"Expected [4, 6, 7, 9], got {sol3}"
  
  problem_solution = resolve(problem)
  print(f"submit {','.join(str(x) for x in problem_solution)}")
  print(f"Total salvado: {len(problem_solution)}")