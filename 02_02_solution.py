import random

def compas(pos_lampe, r):
  x0, y0 = pos_lampe
  for y in range(0, params['h']):
    for x in range(0, params['l']):
      dx, dy = x - x0, y - y0
      if dx*dx/4 + dy*dy < r*r:
        campus[y][x] = rampes[campus[y][x]]

def map_pos(d):
  return random.randrange(params[d])

tampons = ' .-=+*#%@@'
rampes = { tampons[i-1]: tampons[i] for i in range(1, len(tampons)) }
params = { 'l':200, 'h':30, 'R': 11, 'r':2, 'n': 7 }
lampes = [ ]
campus = [ ]

for i in range(params['h']):
  campus.append([ ' ' for i in range(params['l'])])

for i in range(params['n']):
  lampes.append((map_pos('l'), map_pos('h')))

for l in lampes:
  for r in range(1, params['R'], params['r']):
    compas(l, r)

for l in campus:
  print(''.join(l))
