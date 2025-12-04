while True:
    try:
        data = list(map(int, input().split()))
    except:
        break
    n = data[0]
    lst = data[1:]
    check = [True] * (n-1)
    for i in range(1, n):
        d = abs(lst[i-1] - lst[i])
        if 1<=d<=n:
            check[d-1] = False
    if not any(check):
        print('Jolly')
    else:
        print('Not jolly')