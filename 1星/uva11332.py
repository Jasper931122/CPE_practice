def f(n):
    if len(str(n)) == 1:
        return n
    sum = 0
    for i in str(n):
        sum += int(i)
    return f(sum)    

while True:
    n = int(input())
    if n == 0:
        break
    print(f(n))