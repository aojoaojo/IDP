f = open("input", "r")
lines = f.read().strip().split('\n')
x, y = [], []
for line in lines:
    x1, x2 = map(int,line.split())
    x.append(x1)
    y.append(x2)

x.sort()
y.sort()

soma = 0

for i in range(len(x)):
    soma += abs(x[i] - y[i])

print(soma)