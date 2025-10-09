while True:
    inp = input()
    if inp == '0':
        break
    n = int(inp)
    if n%11 == 0:
        print(f'{inp} is a multiple of 11.')
    else:
        print(f'{inp} is not a multiple of 11.')