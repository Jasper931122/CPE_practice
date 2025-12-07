cs = 0
for _ in range(int(input())):
    a = int(input())
    b = int(input())
    if a%2 == 0:
        a += 1
    ans = 0
    for i in range(a, b+1, 2):
        ans += i
    cs += 1
    print(f'Case {cs}: {ans}')