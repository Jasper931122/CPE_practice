code = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('Z')+1)] + [chr(x) for x in range(ord('a'), ord('z')+1)]

while True:
    try:
        n = input()
    except:
        break
    mx = 0
    total = 0
    for i in n:
        tmp = code.index(i)
        total += tmp
        mx = max(mx, tmp)
    for i in range(mx, 62):
        if total%i == 0:
            print(i+1)
            break
    else:
        print('such number is impossible!')