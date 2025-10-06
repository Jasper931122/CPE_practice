<<<<<<< HEAD
=======
<<<<<<< HEAD
def max_cover(lst, s):
    MAX = 10000
    dp = [float('inf')] * MAX
    dp[0] = 0
    for i in range(1, MAX+1):
        dp[i] = min(
            (1 + dp[i-j]) for j in lst if i >= j
        ) if any(j <= i for j in lst) else float('inf')
        if dp[i] > s:
            return i - 1
    return

while True:
    s = int(input())
    if not s:
        break
    max_value = -1
    best_set = None
    for _ in range(int(input())):
        stamps = list(map(int, input().split()))
        stamps.pop(0)
        val = max_cover(stamps, s)
        if val > max_value:
            max_value = val
            best_set = stamps
        elif val == max_value:
            if len(stamps) < len(best_set):
                best_set = stamps
            elif len(stamps) == len(best_set) and stamps[-1] < best_set[-1]:
                best_set = stamps
    frm = lambda x: f'{x:>3}'
=======
>>>>>>> c0e8d1b (2025/10/06)
def max_cover(lst, s):
    MAX = 10000
    dp = [float('inf')] * MAX
    dp[0] = 0
    for i in range(1, MAX+1):
        dp[i] = min(
            (1 + dp[i-j]) for j in lst if i >= j
        ) if any(j <= i for j in lst) else float('inf')
        if dp[i] > s:
            return i - 1
    return

while True:
    s = int(input())
    if not s:
        break
    max_value = -1
    best_set = None
    for _ in range(int(input())):
        stamps = list(map(int, input().split()))
        stamps.pop(0)
        val = max_cover(stamps, s)
        if val > max_value:
            max_value = val
            best_set = stamps
        elif val == max_value:
            if len(stamps) < len(best_set):
                best_set = stamps
            elif len(stamps) == len(best_set) and stamps[-1] < best_set[-1]:
                best_set = stamps
    frm = lambda x: f'{x:>3}'
<<<<<<< HEAD
=======
>>>>>>> c8c7349 (10/06)
>>>>>>> c0e8d1b (2025/10/06)
    print(f'max coverage ={max_value:>4} :{"".join(map(frm, best_set))}')