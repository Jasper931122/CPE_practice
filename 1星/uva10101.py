def bangla(n):
    if n >= 10000000:
        bangla(n//10000000)
        print(' kuti', end='')
        n %= 10000000
    if n >= 100000:
        print(f' {n//100000} lakh', end='')
        n %= 100000
    if n >= 1000:
        print(f' {n//1000} hajar', end='')
        n %= 1000
    if n >= 100:
        print(f' {n//100} shata', end='')
        n %= 100
    if n != 0:
        print(f' {n}', end='')

cs = 0
while True:
    try:
        n = int(input())
    except:
        break
    cs += 1
    print(f'{cs:>4}.', end='')
    if n == 0:
        print(' 0')
    else:
        bangla(n)
        print()