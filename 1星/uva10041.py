for _ in range(int(input())):
    lst = list(map(int, input().split()))
    n = lst.pop(0)
    lst.sort()
    mid = lst[n//2]
    print(int(sum([abs(x-mid) for x in lst])))