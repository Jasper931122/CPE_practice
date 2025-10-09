while True:
    try:
        n, m = map(int, input().split())
        print(abs(m-n))
    except:
        break