def count_zero_cross(start, step, direction):
    # direction: 'R' vagy 'L'
    if direction == 'R':
        first = (100 - start) % 100
    else:  # 'L'
        first = start % 100

    if first == 0:
        first = 100

    if step < first:
        return 0
    return 1 + (step - first) // 100


poz = 50
passwd = 0

with open("input2.txt") as f:
    for line in f:
        dirc = line[0]
        step = int(line[1:])
        passwd += count_zero_cross(poz, step, dirc)
        poz = (poz + (step if dirc == 'R' else -step)) % 100

print("Password (method 0x434C49434B):", passwd)
