import re
invalid = 0


def is_repeating_pattern(szoveg):
    """Igaz, ha a szám ismétlődő mintázatból áll"""
    # Üres vagy 1 karakter nem lehet ismétlődő minta
    if len(szoveg) < 2:
        return False

    # Regex: ^(.+?)\1+$ - bármilyen minta ami legalább 1x ismétlődik
    pattern = re.compile(r'^(.+?)\1+$')
    return bool(pattern.match(szoveg))

with open('input1.txt', 'r') as f:
  for sor in f:
    s = sor.split(',')
    for part in s:
      start, end = list(map(int,part.split('-')))
      for i in range(start, end+1):
        compare = str(i)
        if is_repeating_pattern(compare):
          invalid += i

print("summ", invalid)
