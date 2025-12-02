while True:
    try:
        lst = list(map(int, input().split()))
    except:
        break
    n = lst.pop(0)
    s = [abs(lst[i]-lst[i+1]) for i in range(n-1)]
    if sorted(s) == [x for x in range(1, n)]:
        print('Jolly')
    else:
        print('Not jolly')