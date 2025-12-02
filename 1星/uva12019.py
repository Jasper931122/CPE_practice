from datetime import date

y = 2011
day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for _ in range(int(input())):
    m, d = map(int, input().split())
    print(day[date(y, m, d).weekday()])