import re

poz = 50
passwd = 0

def dial(poz, direction, step):
  if direction == 'R':
    poz = (poz + step) % 100
  elif direction == 'L':
    poz = (poz - step) % 100
  return poz

with open('input1.txt', 'r') as f:
  for sor in f:
    s = sor.strip()
    if s and len(s) >= 2:
      #print(f"{s[0]}, {int(s[1:])}")
      poz = dial(poz, s[0], int(s[1:]))
      if poz == 0:
        passwd += 1


print("Pozition", poz)
print("Password", passwd)
