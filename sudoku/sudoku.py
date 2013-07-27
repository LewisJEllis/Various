"""
Lewis Ellis - ellisl@seas.upenn.edu

CSP-based Sudoku Solver, implementing AC3, forward checking, and back tracking search

My first substantial work in Python. Main impression: list comprehensions are pretty cool. 70 lines can do a lot.

"""


import copy, Queue
regions = ([['c'+str(i)+str(j) for i in range(0,9)] for j in range(0,9)] + # columns - these are the forward checking sets
           [['c'+str(j)+str(i) for i in range(0,9)] for j in range(0,9)] + # rows
           [['c'+str(i)+str(j) for i in range(3*y,3*y+3) for j in range(3*x, 3*x+3)] for x in range(0,3) for y in range(0,3)]) # boxes

class csp: # object which holds the state of a board
  def __init__(self, domains, arcs, constraint):
    self.domains = domains # key -> [1-9]
    self.arcs = arcs # key -> [neighbor, neighbor, ...]
    self.constraint = constraint # function(i,j) returns true if i,j satisfy the constraint

def readSudoku(file):
  def boxRange(x): return range((x/3)*3,(x/3)*3+3) #
  def constraint(i, j): return (i != j)
  def arcgen(x,y): # generates a list of the keys which x,y constrains
    return ['c'+str(i)+str(j) for i in range(0,9) for j in range(0,9) if 
            (i != x or y != j) and (i == x or j == y or (i in boxRange(x) and j in boxRange(y)))]
  data = [('c'+str(i)+str(j), c) for i, line in enumerate(open(file)) for j, c in enumerate(line[0:-1])]
  domains = {key: (range(1,10) if c == '*' else [int(c)]) for (key, c) in data}
  arcs = {key: arcgen(int(key[1]),int(key[2])) for (key, c) in data}
  return csp(domains, arcs, constraint)

def printSudoku(csp): # print the board state nicely
  out = [range(0,9) for i in range(0,9)]
  for x in csp.domains:
    out[int(x[1])][int(x[2])] = str(csp.domains[x][0]) if len(csp.domains[x]) == 1 else "*"
  for x in out: print (''.join(x))

def removeInconsistent(csp, i, j): # Standard AC3 with its helper method, based on AIMA pseudocode
  removed = False
  for x in csp.domains[i][:]:
    if not any([csp.constraint(x, y) for y in csp.domains[j]]):
      csp.domains[i].remove(x)
      removed = True
  return removed

def AC3(csp):
  queue = [(i, j) for i in csp.domains for j in csp.arcs[i]]
  while queue:
    i, j = queue.pop()
    if removeInconsistent(csp, i, j):
        for k in csp.arcs[i]:
          if i != k: queue.append((k, i))

def solveForward(csp):
  changed = True
  while changed:
    AC3(csp)
    changed = False
    for r in regions: # for each region (row, column, box)
      domain = range(1,10)
      [domain.remove(csp.domains[k][0]) for k in r if len(csp.domains[k]) == 1]
      for d in domain: # iterate over the values which haven't been assigned in that value
        if sum(csp.domains[k].count(d) for k in r) == 1:
          csp.domains[[k for k in r if csp.domains[k].count(d) > 0][0]] = [d] # if only one cell can have that value, assign it
          changed = True

def solveDFS(csp):
  q = Queue.LifoQueue()
  q.put(copy.deepcopy(csp))
  while q:
    node = q.get()
    solveForward(node) # use forward checking as a subroutine for each node
    if all([len(node.domains[k]) == 1 for k in node.domains]): # if solved, return
      return node
    if not any([len(node.domains[k]) == 0 for k in node.domains]): # if the node is potentially solvable (no domains are empty)
      guessKey = [k for k in node.domains if len(node.domains[k]) > 1][0] # pick a cell to guess on
      for guess in node.domains[guessKey]: # add each guess to the queue
        successor = copy.deepcopy(node)
        successor.domains[guessKey] = [guess]
        q.put(successor)

printSudoku(solveDFS(readSudoku('tests/diabolical_sudoku')))