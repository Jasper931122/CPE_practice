cs = 0
while True:
    try:
        n = int(input())
        s = list(map(int, input().split()))
    except:
        break
    cs += 1
    cmb = []
    is_b2 = True
    for i in range(n):
        for j in range(i, n):
            p = s[i] + s[j]
            if p not in cmb:
                cmb.append(p)
            else:
                is_b2 = False
                break
    if is_b2:
        print(f'Case #{cs}: It is a B2-Sequence.')
    else:
        print(f'Case #{cs}: It is not a B2-Sequence.')