cs = 0
while True:
    n, r = map(int, input().split())
    if not (n or r):
        break
    cities = set()
    edges = []
    for _ in range(r):
        a, b, t = input().split()
        t = int(t)
        cities.add(a)
        cities.add(b)
        edges.append((a, b, t))
        edges.append((b, a, t))
    st, en = input().split()
    
    city_num = {j:i for i, j in enumerate(cities)}

    cost = [0]*n
    cost[city_num[st]] = float('inf')
    visted = [False]*n
    que = [(cost[city_num[st]], st)]
    while que:
        c, x = que.pop(0)
        if visted[city_num[x]]:
            continue
        visted[city_num[x]] = True
        if x == en:
            break
        for a, b, t in edges:
            if a == x:
                min_cost = min(t, cost[city_num[x]])
                if min_cost > cost[city_num[b]]:
                    cost[city_num[b]] = min_cost
                    que.append((min_cost, b))
        que.sort(key= lambda x: -x[0])
    cs+=1
    print(f'Scenario #{cs}')
    print(f'{cost[city_num[en]]} tons')
    print()