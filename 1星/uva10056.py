a = int(input())

for i in range(a):
    n, p, t = map(float, input().split())
    q = 1 - p
    ans = q**(t-1)*p/(1-q**n)
    print(round(ans, 4))