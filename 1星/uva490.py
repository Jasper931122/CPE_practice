lst = []
max_len = 0
while True:
    try:
        s = input()
        lst.append(s)
        max_len = max(max_len, len(s))
    except:
        break
lst = lst[::-1]
for i in range(len(lst)):
    lst[i] = lst[i].ljust(max_len, ' ')

for i in range(max_len):
    for j in range(len(lst)):
        print(lst[j][i], end='')
    print()