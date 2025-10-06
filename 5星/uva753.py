def hopcroft_krap(adj, n_left, n_right):
    pair_u = [-1]*n_left
    pair_v = [-1]*n_right
    dist = [0]*n_left

    def bfs():
        que = []
        for u in range(n_left):
            if pair_u[u] == -1:
                dist[u] = 0
                que.append(u)
            else:
                dist[u] = float('inf')
        found = False
        while que:
            u = que.pop(0)
            for v in adj[u]:
                pu = pair_v[v]
                if pu == -1:
                    found = True
                elif dist[pu] == float('inf'):
                    dist[pu] = dist[u] + 1
                    que.append(pu)
        return found

    def dfs(u):
        for v in adj[u]:
            pu = pair_v[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = 10**9
        return False
    
    matching = 0
    while bfs():
        for u in range(n_left):
            if pair_u[u] == -1 and dfs(u):
                matching += 1
    return matching

first_case = True
for _ in range(int(input())):
    input()
    n = int(input())
    recept_types = []
    for _ in range(n):
        recept_types.append(input())
    m = int(input())
    devices = []
    for _ in range(m):
        devices.append(input().split()[1])
    k = int(input())
    adapters = []
    for _ in range(k):
        adapters.append(input().split())

    all_types = set(recept_types) | set(devices)
    for a, b in adapters:
        all_types.add(a)
        all_types.add(b)
    type_list = sorted(all_types)
    tid = {t:i for i, t in enumerate(type_list)}
    T = len(type_list)

    g = [[] for _ in range(T)]
    for i in range(T):
        g[i].append(i)
    for a, b in adapters:
        g[tid[b]].append(tid[a])

    reach = [set() for _ in range(T)]
    for s in range(T):
        q = [s]
        seen = [False]*T
        seen[s] = True
        while q:
            u = q.pop(0)
            reach[s].add(u)
            for w in g[u]:
                if not seen[w]:
                    seen[w] = True
                    q.append(w)

    left_types = [tid[t] for t in recept_types]
    right_types = [tid[p] for p in devices]

    adj = [[] for _ in range(n)]
    for u in range(n):
        rtype = left_types[u]
        reachable_set = reach[rtype]
        for v in range(m):
            ptype = right_types[v]
            if ptype in reachable_set:
                adj[u].append(v)

    if first_case:
        first_case = False
    else:
        print()
    print(m - hopcroft_krap(adj, n, m))