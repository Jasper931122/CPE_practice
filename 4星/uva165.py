<<<<<<< HEAD
=======
<<<<<<< HEAD
def max_cover(lst, h):
    MAX = 10000
    tmp = [0] + [float('inf')]*MAX
    for i in range(1, MAX+1):
        tmp[i] = min(
            (1 + tmp[i-j]) for j in lst if i >= j
        ) if any(j <= i for j in lst) else float('inf')
        if tmp[i] > h:
            return i - 1
    return MAX

def search(h, k):
    best_n, best_set = 0, None

    def dfs(values, start):
        nonlocal best_n, best_set
        n = max_cover(values, h)
        if len(values) == k:
            if n > best_n:
                best_n, best_set = n, values[:]
            return
        for nxt in range(start, n + 2):
            dfs(values + [nxt], nxt + 1)

    dfs([1], 2)
    return best_n, best_set

while True:
    h, k = map(int, input().split())
    if h==0 and k==0:
        break
    best_n, best_set = search(h, k)
    fmt = lambda x: f'{x:>3}'
=======
>>>>>>> c0e8d1b (2025/10/06)
def max_cover(lst, h):
    MAX = 10000
    tmp = [0] + [float('inf')]*MAX
    for i in range(1, MAX+1):
        tmp[i] = min(
            (1 + tmp[i-j]) for j in lst if i >= j
        ) if any(j <= i for j in lst) else float('inf')
        if tmp[i] > h:
            return i - 1
    return MAX

def search(h, k):
    best_n, best_set = 0, None

    def dfs(values, start):
        nonlocal best_n, best_set
        n = max_cover(values, h)
        if len(values) == k:
            if n > best_n:
                best_n, best_set = n, values[:]
            return
        for nxt in range(start, n + 2):
            dfs(values + [nxt], nxt + 1)

    dfs([1], 2)
    return best_n, best_set

while True:
    h, k = map(int, input().split())
    if h==0 and k==0:
        break
    best_n, best_set = search(h, k)
    fmt = lambda x: f'{x:>3}'
<<<<<<< HEAD
=======
>>>>>>> c8c7349 (10/06)
>>>>>>> c0e8d1b (2025/10/06)
    print(f'{"".join(map(fmt, best_set))} ->{best_n:>3}')