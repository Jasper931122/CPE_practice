cmb = [0] * 30001
cmb[0] = 1

coin = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

for i in coin:
    for j in range(i, 30001, 5):
        cmb[j] += cmb[j-i]

while True:
    s = input().strip()
    n = int(s.replace('.', ''))
    if n == 0:
        break
cmb = [0] * 30001
cmb[0] = 1

coin = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

for i in coin:
    for j in range(i, 30001, 5):
        cmb[j] += cmb[j-i]

while True:
    s = input().strip()
    n = int(s.replace('.', ''))
    if n == 0:
        break
    print(f'{s:>6}{cmb[n]:>17}')