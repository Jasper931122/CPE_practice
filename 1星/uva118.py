o = ['N', 'E', 'S', 'W']
dir = {'N':(0, 1), 'E':(1, 0), 'S':(0, -1), 'W':(-1, 0)}

n, m = map(int, input().split())
scent= []
while True:
    try:
        x, y, d = input().split()
        x = int(x); y = int(y)
        cmd = input()
    except:
        break
    lost = False
    for i in cmd:
        if i == 'L':
            d = o[(o.index(d)-1)%4]
        elif i == 'R':
            d = o[(o.index(d)+1)%4]
        else:
            dx, dy = dir[d]
            nx, ny = x+dx, y+dy
            if nx > n or ny > m or nx < 0 or ny < 0:
                if (x, y) in scent:
                    continue
                else:
                    lost = True
                    scent.append((x, y))
                    break
            else:
                x, y = nx, ny
    if lost:
        print(f'{x} {y} {d} LOST')
    else:
        print(f'{x} {y} {d}')