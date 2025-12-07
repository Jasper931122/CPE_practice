for _ in range(int(input())):
    s, d = map(int, input().split())
    a = (s+d)//2
    b = s-a
    if s >= 0 and b >= 0:
        print(a, b)
    else:
        print('impossible')