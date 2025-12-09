a = "34567890-=ertyuiop[]\dfghjkl;'cvbnm,./"
b = "1234567890qwertyuiop[asdfghjklzxcvbnm,"

while True:
    try:
        s = list(input().lower())
    except:
        break
    for i in s:
        if i != ' ':
            idx = a.index(i)
            print(b[idx], end='')
        else:
            print(' ', end='')
    print()