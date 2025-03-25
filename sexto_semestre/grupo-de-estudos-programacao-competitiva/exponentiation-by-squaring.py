def squaring(a,b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return squaring((a*a) % 10 ,b//2) % 10
    elif b % 2 == 1:
        return a * squaring((a*a) % 10,(b-1)//2) % 10

n = int(input())
for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(squaring(a,b))