summa = 0

with open('input1.txt', 'r') as f:
    for sor in f:
        #for n in range(len(sor)-1):
        maximum= 0
        for n, h in enumerate(sor[:-1], 0):
            for n2, h2 in enumerate(sor[n+1:]):
                h3 = int(str(h) + str(h2))
               if h3 > maximum:
                 maximum = h3
                 summa += maximum
print("summ", summa)
