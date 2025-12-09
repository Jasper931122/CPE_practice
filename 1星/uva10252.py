while True:
    try:
        a = input()
        b = input()
    except:
        break
    for i in range(65, 91):
        c = chr(i)
        cnt = min(a.count(c), b.count(c))
        print(c*cnt, end='')
    print()