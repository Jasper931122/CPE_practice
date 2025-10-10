# print(ord('A'))

string = ''
for _ in range(int(input())):
    string += input().upper()

dic = {}
for i in range(65, 91):
    alp = chr(i)
    cnt = string.count(alp)
    if cnt > 0:
        dic[alp] = cnt

lst = []
for i in dic:
    lst.append((i, dic[i]))

lst.sort(key=lambda x:-x[1])
for i, j in lst:
    print(i, j)