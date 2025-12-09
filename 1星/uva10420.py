dic = {}
n = int(input())
for _ in range(n):
    cnt = input().split()[0]
    if cnt not in dic:
        dic[cnt] = 1
    else:
        dic[cnt] += 1
lst = sorted(dic.keys())
for i in lst:
    print(i, dic[i])