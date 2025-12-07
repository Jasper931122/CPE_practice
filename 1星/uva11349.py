t = 0
for _ in range(int(input())):
    n = int(input().split()[-1])
    arr = ''
    for _ in range(n):
        arr += input().replace(' ', '')
    t += 1
    if arr == arr[::-1]:
        print(f'Test #{t}: Symmetric.')
    else:
        print(f'Test #{t}: Non-symmetric.')