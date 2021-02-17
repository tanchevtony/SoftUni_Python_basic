first = int(input())
second = int(input())

f1 = first // 1000
f2 = first // 100 % 10
f3 = first // 10 % 10
f4 = first % 10

s1 = second // 1000
s2 = second // 100 % 10
s3 = second // 10 % 10
s4 = second % 10

for i in range(f1, s1 + 1):
    for j in range(f2, s2 + 1):
        for k in range(f3, s3 + 1):
            for m in range(f4, s4 + 1):

                if i % 2 != 0 or i == 1 and f1 <= i <= s1:
                    if j % 2 != 0 or j == 1 and f2 <= j <= s2:
                        if k % 2 != 0 or k == 1 and f3 <= k <= s3:
                            if m % 2 != 0 or m == 1 and f4 <= m <= s4:
                                print(f"{i}{j}{k}{m}", end=" ")
