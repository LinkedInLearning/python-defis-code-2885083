import random

def spam_co(spam_elpo, r):
  x0, y0 = spam_elpo
  for y in range(0, spam_ra['h']):
    for x in range(0, spam_ra['l']):
      dx, dy = x - x0, y - y0
      if dx*dx/4 + dy*dy < r*r:
        spam_uc[y][x] = spam_re[spam_uc[y][x]]

def spam_op(d):
  return random.randrange(spam_ra[d])

spam_ton = ' .-=+*#%@@'
spam_re = { spam_ton[i-1]: spam_ton[i] for i in range(1, len(spam_ton)) }
spam_ra = { 'l':200, 'h':30, 'R': 11, 'r':2, 'n': 7 }
spam_le = [ ]
spam_uc = [ ]

for i in range(spam_ra['h']):
  spam_uc.append([ ' ' for i in range(spam_ra['l'])])

for i in range(spam_ra['n']):
  spam_le.append((spam_op('l'), spam_op('h')))

for l in spam_le:
  for r in range(1, spam_ra['R'], spam_ra['r']):
    spam_co(l, r)

for l in spam_uc:
  print(''.join(l))
