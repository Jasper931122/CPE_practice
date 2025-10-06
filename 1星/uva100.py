'''
簡單暴力解，放到Uva評分系統會超時，但應付CPE應該OK
while True:
    try:
        n, m = map(int, input().split())
    except:
        break
    max_cycle = 0
    print(f'{n} {m} ', end='')
    if n > m:
        n, m = m, n
    for i in range(n, m+1):
        cycle = 1
        while i != 1:
            if i % 2:
                i = i*3+1
            else:
                i = i//2
            cycle += 1
        max_cycle = max(max_cycle, cycle)
    print(max_cycle)
'''

table = {}
def dp(n):
    if n == 1:
        return 1
    if n in table:
        return table[n]
    if n % 2:
        nxt_n = 3*n+1
    else:
        nxt_n = n//2
    table[n] = 1 + dp(nxt_n)
    return table[n]

while True:
    try:
        n, m = map(int, input().split())
    except:
        break
    max_cycle = 0
    print(f'{n} {m} ', end='')
    if n > m:
        n, m = m, n
    for i in range(n, m+1):
        max_cycle = max(max_cycle, dp(i))
    print(max_cycle)