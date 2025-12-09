while True:
    n = int(input())
    if n==0:
        break
    b = bin(n)[2:]
    print(f'The parity of {b} is {b.count("1")} (mod 2).')