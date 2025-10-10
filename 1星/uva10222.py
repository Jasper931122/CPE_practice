a = "34567890-=ertyuiop[]\dfghjkl;'cvbnm,./"
b = "1234567890qwertyuiop[asdfghjklzxcvbnm,"

while True:
    try:
        s = list(input().lower())
    except:
        break
    for i in range(len(s)):
        if s[i] != ' ':
            s[i] = b[a.index(s[i])]
    print(''.join(s))