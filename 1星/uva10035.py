while True:
    a, b = input().split()
    if a == '0' and b == '0':
        break
    a = a[::-1]; b = b[::-1]
    a_len = len(a); b_len = len(b)
    dis = abs(a_len-b_len)
    if a_len > b_len:
        b += '0'*dis
    else:
        a += '0'*dis
    cnt = 0
    carry = 0
    for i in range(len(a)):
        carry = (int(a[i])+int(b[i])+carry)//10
        if carry:
            cnt += 1

    if cnt == 0:
        print('No carry operation.')
    elif cnt == 1:
        print('1 carry operation.')
    else:
        print(f'{cnt} carry operations.')