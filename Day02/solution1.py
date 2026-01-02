invalid = 0

def eleje_vege_egyezik(szoveg):
    """Igaz, ha van legalább 1 egyező rész az elején és a végén"""
    if len(szoveg) % 2 != 0:
        return False
    else:
      h = int(len(szoveg)/2)
      #print(type(szoveg), szoveg, h)
      if szoveg[:h] == szoveg[h:]:
        return True

    # Végigmegyünk az összes lehetséges hosszon
    #for hossz in range(1, len(szoveg)//2 + 1):
    #    if szoveg[:hossz] == szoveg[-hossz:]:
    #        return True
    return False

with open('input1.txt', 'r') as f:
  for sor in f:
    s = sor.split(',')
    for part in s:
      start, end = list(map(int,part.split('-')))
      for i in range(start, end+1):
        compare = str(i)
        if eleje_vege_egyezik(compare):
          invalid += i

print("summ", invalid)
