flag = True
while True:
    try:
        line = input()
    except:
        break
    tmp = list(line)
    for i in range(len(line)):
        if line[i] == '"':
            if flag:
                tmp[i] = "``"
            else:
                tmp[i] = "''"
            flag = not flag
    print(''.join(tmp))