from collections import Counter

f = open("input", "r")
lines = f.read().strip().split('\n')
x, y = [], []
for line in lines:
    x1, x2 = map(int,line.split())
    x.append(x1)
    y.append(x2)

soma = 0

l = Counter(y)

for elemento in x:
    soma = soma + (elemento * l[elemento])

print(soma)