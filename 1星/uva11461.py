while True:
    a, b = map(int, input().split())
    if a==0 and b==0:
        break
    cnt = 0
    check = False
    for i in range(1, int(100000**0.5)+1):
        if i**2 > b:
            break
        if check:
            cnt += 1
        elif i**2 >= a:
            check = True
            cnt = 1
    print(cnt)