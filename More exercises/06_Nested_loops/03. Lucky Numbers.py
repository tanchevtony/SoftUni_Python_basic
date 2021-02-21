n = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for m in range(1, 10):
                sum_first_pair = i + j
                sum_second_pair = k + m
                if sum_first_pair == sum_second_pair:
                    if n % sum_first_pair == 0:
                        print(f"{i}{j}{k}{m}", end=" ")
