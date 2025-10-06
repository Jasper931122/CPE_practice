<<<<<<< HEAD
=======
<<<<<<< HEAD
data = []
while True:
    try:
        data.append(input())
    except:
        break
data = ' '.join(data)
s = data.replace('()', 'end').replace('(', '').replace(')', '').split('end')
s.pop()
for i in s:
    i = i.strip().split()
    nodes = [x.replace(' ', '').split(',') for x in i]
    nodes.sort(key=lambda x: (len(x[1]), x[1]))
    ln = len(nodes)
    n = [x[0] for x in nodes]
    e = [x[1] for x in nodes]
    if len(set(e)) != len(n):
        print('not complete')
    elif ln == 1 and e[0] != '':
        print('not complete')
    else:
        for i in range(1, ln):
            if e[i][:-1] not in e[:i]:
                print('not complete')
                break
        else:
=======
>>>>>>> c0e8d1b (2025/10/06)
data = []
while True:
    try:
        data.append(input())
    except:
        break
data = ' '.join(data)
s = data.replace('()', 'end').replace('(', '').replace(')', '').split('end')
s.pop()
for i in s:
    i = i.strip().split()
    nodes = [x.replace(' ', '').split(',') for x in i]
    nodes.sort(key=lambda x: (len(x[1]), x[1]))
    ln = len(nodes)
    n = [x[0] for x in nodes]
    e = [x[1] for x in nodes]
    if len(set(e)) != len(n):
        print('not complete')
    elif ln == 1 and e[0] != '':
        print('not complete')
    else:
        for i in range(1, ln):
            if e[i][:-1] not in e[:i]:
                print('not complete')
                break
        else:
<<<<<<< HEAD
=======
>>>>>>> c8c7349 (10/06)
>>>>>>> c0e8d1b (2025/10/06)
            print(' '.join(n))