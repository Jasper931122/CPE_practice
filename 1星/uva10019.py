for _ in range(int(input())):
    m = input()
    b1 = bin(int(m)).count('1')
    b2 = bin(int(m, 16)).count('1')
    print(b1, b2)