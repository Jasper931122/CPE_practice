while True:
    try:
        a = input()
        b = input()
    except:
        break
    a_set = set(a)
    lst = []
    for i in a_set:
        cnt = min(a.count(i), b.count(i))
        if cnt > 0:
            lst.append((i, cnt))
    lst.sort(key= lambda x: x[0])
    for i, t in lst:
        print(i*t, end='')
    print()