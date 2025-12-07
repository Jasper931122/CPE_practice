while True:
    try:
        s, d = map(int, input().split())
    except:
        break
    cnt = s
    while cnt < d:
        s += 1
        cnt += s
    print(s)