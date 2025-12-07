while True:
    try:
        a = int(input())
        lst = list(map(int, input().split()))[::-1]
    except:
        break
    ans = 0
    for i in range(1, len(lst)):
        ans += lst[i]*i*a**(i-1)

    print(ans)