n = input()

one = int(n[2])
two = int(n[1])
three = int(n[0])

for i in range(1, one + 1):
    for j in range(1, two + 1):
        for h in range(1, three + 1):
            print(f'{i}*{j}*{h}={i * j * h}')