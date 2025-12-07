fib = [1, 2]
while True:
    fib.append(fib[-1]+fib[-2])
    if fib[-1] > 100000000:
        break

for _ in range(int(input())):
    n = int(input())
    print(f'{n} = ', end='')
    fnd = False
    for i in fib[::-1]:
        if i <= n:
            n -= i
            fnd = True
            print(1, end='')
        elif fnd:
            print(0, end='')
    print(' (fib)')